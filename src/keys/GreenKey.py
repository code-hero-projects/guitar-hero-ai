from keys.BaseKey import BaseKey
from keys.RGB import RGB
from keys.KeyBound import KeyBound


class GreenKey(BaseKey):
  def __init__(self) -> None:
    super().__init__(KeyBound(0, 170), RGB(0, 206, 0), RGB(20, 255, 20), 'q', 'green')
