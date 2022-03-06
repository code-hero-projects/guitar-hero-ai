from keys.BaseKey import BaseKey
from keys.HSV import HSV
from keys.KeyBound import KeyBound


class RedKey(BaseKey):
  def __init__(self) -> None:
    super().__init__(KeyBound(180, 350), HSV(0, 209, 48), HSV(179, 255, 255), 'w')
