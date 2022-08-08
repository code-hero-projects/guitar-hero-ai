from keys.BaseKey import BaseKey
from keys.HSV import HSV
from keys.KeyBound import KeyBound
from keys.KeyLocation import KeyLocation


class OrangeKey(BaseKey):
  def __init__(self) -> None:
    super().__init__(KeyBound(740, 880), HSV(19, 128, 98), HSV(60, 255, 255), 't', 'orange')
