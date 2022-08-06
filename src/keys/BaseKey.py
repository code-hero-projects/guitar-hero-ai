import threading
import time

import cv2
import keyboard
import numpy as np

from keys.KeyBound import KeyBound
from keys.NoteTypeEnum import NoteTypeEnum
from keys.RGB import RGB


class BaseKey:
  def __init__(self, key_bound: KeyBound, lower_bound_rgb: RGB, upper_bound_rgb: RGB, key_to_press: str, color: str) -> None:
    self._key_bound = key_bound
    self._lower_bound_rgb = lower_bound_rgb
    self._upper_bound_rgb = upper_bound_rgb
    self._key_to_press = key_to_press
    self._color = color
    self._key_pressed = False
    self._previous_note = NoteTypeEnum.NONE

  def write_to_file(self, screenshot_number, image, mask):
    filename_image = f'note-{screenshot_number}-{self._color}.png'
    #filename_mask = f'note-{screenshot_number}-{self._color}-mask.png'
    cv2.imwrite(filename_image, image)
    #cv2.imwrite(filename_mask, mask)

  def handle_screenshot(self, image, screenshot_number):
    key_bound = KeyBound(self._key_bound.end -30, self._key_bound.end - 5)
    key_image = self._get_image_in_range(image, key_bound)

    current_note = self._get_current_note(key_image)

    if current_note == NoteTypeEnum.NONE:
      self._release()
    elif current_note == NoteTypeEnum.SINGLE_NOTE:
      if self._previous_note == NoteTypeEnum.NONE:
        self._press()
      # elif self._previous_note == NoteTypeEnum.LINE:
      #   self._release()
    
    self._previous_note = current_note

    self._save_image(screenshot_number, image, None)
    # side_key = self._get_image_in_range(image, key_bound)
    
    # current_note = self._get_current_note(mask)
    # if current_note == NoteTypeEnum.NONE:
    #   self._release()
    # elif current_note == NoteTypeEnum.SINGLE_NOTE:
    #   if self._previous_note == NoteTypeEnum.NONE:
    #     self._press()
    #   elif self._previous_note == NoteTypeEnum.LINE:
    #     self._release()

        # the code runs too fast so the game doesn't detect the release
        # time.sleep(0.01)
        # self._press()
      # note = self._get_image_in_range(key_image, KeyBound(5, 30))
      # print(note)
      # self._save_image(screenshot_number, note, mask)
  
    # self._previous_note = current_note

  def _press(self):
    if not self._key_pressed:
      keyboard.press(self._key_to_press)
      self._key_pressed = True
  
  def _release(self):
    if self._key_pressed:
      keyboard.release(self._key_to_press)
      self._key_pressed = False

  def _get_current_note(self, key_image):
    for pixels2d in key_image:
      for pixel in pixels2d:
        if (self._is_in_bound(pixel)):
          return NoteTypeEnum.SINGLE_NOTE
    return NoteTypeEnum.NONE
    # if np.count_nonzero(mask) == 0:
    #   return NoteTypeEnum.NONE
    
    # note = self._get_image_in_range(mask, KeyBound(0, 30))
    # note_count = np.count_nonzero(note)
    # if note_count > 0:
    #   return NoteTypeEnum.SINGLE_NOTE
    # else:
    #   line = self._get_image_in_range(mask, KeyBound(80, 90))
    #   note_count = np.count_nonzero(line)
    #   return NoteTypeEnum.LINE

  def _is_in_bound(self, pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    return self._lower_bound_rgb.red <= red <= self._upper_bound_rgb.red and\
      self._lower_bound_rgb.green <= green <= self._upper_bound_rgb.green and\
      self._lower_bound_rgb.blue <= blue <= self._upper_bound_rgb.blue

  def _get_image_in_range(self, image, key_bound: KeyBound):
    pixels_rows = []

    for pixel_line in image:
      rows_to_append = pixel_line[key_bound.start:key_bound.end]
      pixels_rows.append(rows_to_append)

    return np.array(pixels_rows)

  def _save_image(self, screenshot_number, key_image, mask):
    thread = threading.Thread(target=self.write_to_file, args=(screenshot_number, key_image, mask), daemon=True)
    thread.start()