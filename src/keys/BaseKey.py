import time

import cv2
import keyboard
import numpy as np
from process_image import get_image_in_range

from keys.HSV import HSV
from keys.KeyBound import KeyBound
from keys.NoteTypeEnum import NoteTypeEnum


class BaseKey:
  def __init__(self, key_bound: KeyBound, lower_bound_hsv: HSV, higher_bound_hsv: HSV, key_to_press: str) -> None:
    self.key_bound = key_bound
    self._lower_bound_hsv = lower_bound_hsv
    self._upper_bound_hsv = higher_bound_hsv
    self._key_to_press = key_to_press
    self._key_pressed = False
    self._previous_note = NoteTypeEnum.NONE

  def handle_screenshot(self, image, filename_img, filename_mask: str) -> bool:
    mask = self._mask_image(image, self._lower_bound_hsv, self._upper_bound_hsv)
    
    current_note = self._get_current_note(mask, filename_mask)

    # if filename_img != '':
    #   cv2.imwrite(filename_img, image)

    if current_note == NoteTypeEnum.NONE:
      self._release()
    elif current_note == NoteTypeEnum.SINGLE_NOTE:
      # print(f'previous {self._previous_note}')
      # print(f'current {current_note}')

      if self._previous_note == NoteTypeEnum.NONE:
        self._press()
      elif self._previous_note == NoteTypeEnum.LINE:
        self._release()

        # the code runs too fast so the game doesn't detect the release
        time.sleep(0.01)
        self._press()
  
    self._previous_note = current_note

  def _press(self):
    if not self._key_pressed:
      # print ('pressed')
      keyboard.press(self._key_to_press)
      self._key_pressed = True
  
  def _release(self):
    if self._key_pressed:
      # print ('released')
      keyboard.release(self._key_to_press)
      self._key_pressed = False

  def _mask_image(self, image, lower_bound_hsv: HSV, upper_bound_hsv: HSV):
    lower_bound = np.array([lower_bound_hsv.hue, lower_bound_hsv.saturation, lower_bound_hsv.value])
    upper_bound = np.array([upper_bound_hsv.hue, upper_bound_hsv.saturation, upper_bound_hsv.value])

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    return mask

  def _get_current_note(self, mask, filename_mask):
    if np.count_nonzero(mask) == 0:
      return NoteTypeEnum.NONE
    
    note = get_image_in_range(mask, KeyBound(0, 30))
    note_count = np.count_nonzero(note)
    # print (f'note_counts: {note_count}')
    if note_count > 0:
      # if filename_mask != '':
      #   cv2.imwrite(filename_mask, note)
      return NoteTypeEnum.SINGLE_NOTE
    else:
      line = get_image_in_range(mask, KeyBound(80, 90))
      note_count = np.count_nonzero(line)
      # print (f'line_counts: {note_count}')
      # if filename_mask != '':
      #   cv2.imwrite(filename_mask, line)
      return NoteTypeEnum.LINE
