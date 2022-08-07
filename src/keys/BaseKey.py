import threading
import time

import cv2
import keyboard
import numpy as np
from process_image import get_image_in_range

from keys.HSV import HSV
from keys.KeyBound import KeyBound
from keys.NoteTypeEnum import NoteTypeEnum


class BaseKey:
  def __init__(self, key_bound: KeyBound, lower_bound_hsv: HSV, higher_bound_hsv: HSV, key_to_press: str, color: str) -> None:
    self._key_bound = key_bound
    self._lower_bound_hsv = lower_bound_hsv
    self._upper_bound_hsv = higher_bound_hsv
    self._key_to_press = key_to_press
    self._color = color
    self._key_pressed = False
    self._previous_note = NoteTypeEnum.NONE

  def write_to_file(self, screenshot_number, image, mask):
    filename_image = f'note-{screenshot_number}-{self._color}.png'
    filename_mask = f'note-{screenshot_number}-{self._color}-mask.png'
    cv2.imwrite(filename_image, image)
    cv2.imwrite(filename_mask, mask)

  def handle_screenshot(self, image, screenshot_number) -> bool:
    key_image = get_image_in_range(image, self._key_bound)
    mask = self._mask_image(key_image, self._lower_bound_hsv, self._upper_bound_hsv)
    
    current_note = self._get_current_note(mask)

    # thread = threading.Thread(target=self.write_to_file, args=(screenshot_number, image, mask), daemon=True)
    # thread.start()

    if current_note == NoteTypeEnum.NONE:
      self._release()
    elif current_note == NoteTypeEnum.SINGLE_NOTE:      
      if self._previous_note == NoteTypeEnum.NONE:
        self._press()
      elif self._previous_note == NoteTypeEnum.LINE:
        self._release()

        # the code runs too fast so the game doesn't detect the release
        time.sleep(0.01)
        self._press()
  
    self._previous_note = current_note

  def get_image_in_range(image, key_bound: KeyBound):
    pixels_rows = []

    for pixel_line in image:
      rows_to_append = pixel_line[key_bound.start:key_bound.end]
      pixels_rows.append(rows_to_append)

    return np.array(pixels_rows)

  def _press(self):
    if not self._key_pressed:
      keyboard.press(self._key_to_press)
      self._key_pressed = True
  
  def _release(self):
    if self._key_pressed:
      keyboard.release(self._key_to_press)
      self._key_pressed = False

  def _mask_image(self, image, lower_bound_hsv: HSV, upper_bound_hsv: HSV):
    lower_bound = np.array([lower_bound_hsv.hue, lower_bound_hsv.saturation, lower_bound_hsv.value])
    upper_bound = np.array([upper_bound_hsv.hue, upper_bound_hsv.saturation, upper_bound_hsv.value])

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    return mask

  def _get_current_note(self, mask):
    if np.count_nonzero(mask) == 0:
      return NoteTypeEnum.NONE
    
    note = get_image_in_range(mask, KeyBound(0, 30))
    note_count = np.count_nonzero(note)
    if note_count > 0:
      return NoteTypeEnum.SINGLE_NOTE
    else:
      line = get_image_in_range(mask, KeyBound(80, 90))
      note_count = np.count_nonzero(line)
      return NoteTypeEnum.LINE
