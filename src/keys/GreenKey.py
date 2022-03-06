from keys.BaseKey import BaseKey
from keys.HSV import HSV
from keys.KeyBound import KeyBound
from keys.KeyLocation import KeyLocation


class GreenKey(BaseKey):
  def __init__(self) -> None:
    super().__init__(KeyBound(0, 170), HSV(44, 141, 100), HSV(60, 255, 255), 'q')
