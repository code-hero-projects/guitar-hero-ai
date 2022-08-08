from keys.BaseKey import BaseKey
from keys.HSV import HSV
from keys.KeyBound import KeyBound


class YellowKey(BaseKey):
  def __init__(self) -> None:
    super().__init__(KeyBound(380, 520), HSV(24, 165, 63), HSV(50, 255, 255), 'e', 'yellow')
