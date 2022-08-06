import threading
import keyboard
import numpy as np

from keys.BlueKey import BlueKey
from keys.GreenKey import GreenKey
from keys.KeyLocation import KeyLocation
from keys.OrangeKey import OrangeKey
from keys.RedKey import RedKey
from keys.YellowKey import YellowKey
from process_image import get_image_from_file, get_image_from_file_to_array
from screenshot import get_screenshot


def thread_func(key, image, screenshot_number):
  key.handle_screenshot(image, screenshot_number)

def play(keys):
  key_location = KeyLocation(1180, 835, 30, 890)
  screenshot_number = 1
  while True:
    image = get_screenshot(key_location)
    for key in keys:
      thread = threading.Thread(target=thread_func, args=(key, image, screenshot_number), daemon=True)
      thread.start()
      screenshot_number += 1

def main():
  print('press s to start')
  keyboard.wait('s')
  print('started')

  keys = [GreenKey(), RedKey(), YellowKey(), BlueKey(), OrangeKey()]
  play(keys)

if __name__ == '__main__':
  main()
