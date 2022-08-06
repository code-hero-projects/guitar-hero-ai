import numpy as np

from keys.BlueKey import BlueKey
from keys.GreenKey import GreenKey
from keys.KeyLocation import KeyLocation
from keys.OrangeKey import OrangeKey
from keys.RedKey import RedKey
from keys.YellowKey import YellowKey
from process_image import get_image_from_file

def main():
  key = RedKey()
  image = np.array(get_image_from_file('note-72-red.png'))
  key.handle_screenshot(image, 0)

if __name__ == '__main__':
  main()
