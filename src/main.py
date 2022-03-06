import threading

import keyboard

from keys.BlueKey import BlueKey
from keys.GreenKey import GreenKey
from keys.KeyLocation import KeyLocation
from keys.OrangeKey import OrangeKey
from keys.RedKey import RedKey
from keys.YellowKey import YellowKey
from process_image import get_image_in_range
from screenshot import get_screenshot


def thread_func(key, image, screenshot_number):
  key.handle_screenshot(image, f'note-{screenshot_number}.png', f'note-{screenshot_number}-mask.png')

def play(keys):
  key_location = KeyLocation(1180, 835, 30, 890)
  screenshot_number = 1
  while True:
    threads = []
    image = get_screenshot(key_location)
    for key in keys:
      key_image = get_image_in_range(image, key.key_bound)
      thread = threading.Thread(target=thread_func, args=(key, key_image, screenshot_number), daemon=True)
      threads.append(thread)
      thread.start()
    
    screenshot_number += 1

def main():
  print('press s to start')
  keyboard.wait('s')
  print('started')

  keys = [GreenKey(), RedKey(), YellowKey(), BlueKey(), OrangeKey()]
  play(keys)

main()
