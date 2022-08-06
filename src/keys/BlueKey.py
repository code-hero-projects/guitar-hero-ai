from keys.BaseKey import BaseKey
from keys.HSV import HSV
from keys.KeyBound import KeyBound


class BlueKey(BaseKey):
  def __init__(self) -> None:
    super().__init__(KeyBound(555, 710), HSV(19, 100, 100), HSV(179, 255, 255), 'r', 'blue')
