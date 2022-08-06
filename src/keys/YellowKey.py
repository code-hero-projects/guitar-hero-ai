from keys.BaseKey import BaseKey
from keys.HSV import HSV
from keys.KeyBound import KeyBound


class YellowKey(BaseKey):
  def __init__(self) -> None:
    super().__init__(KeyBound(380, 520), HSV(24, 149, 63), HSV(179, 255, 255), 'e', 'yellow')
