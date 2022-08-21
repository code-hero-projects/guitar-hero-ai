from keys.BaseKey import BaseKey
from keys.HSV import HSV
from keys.KeyBound import KeyBound


class RedKey(BaseKey):
  def __init__(self) -> None:
    super().__init__(KeyBound(200, 340), KeyBound(110, 140), HSV(0, 190, 125), HSV(52, 255, 255), 'w', 'red')
