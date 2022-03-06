import numpy
from mss import mss, tools

from keys.KeyLocation import KeyLocation


def get_screenshot(keyLocation: KeyLocation):
  with mss() as sct:
    monitor = { "top": keyLocation.top, "left": keyLocation.left, "height": keyLocation.height, "width": keyLocation.width }
    sct_img = sct.grab(monitor)
    return numpy.array(sct_img)

def get_image(keyLocation: KeyLocation):
  with mss() as sct:
    monitor = { "top": keyLocation.top, "left": keyLocation.left, "height": keyLocation.height, "width": keyLocation.width }
    sct_img = sct.grab(monitor)
    return tools.to_png(sct_img.rgb, sct_img.size)
