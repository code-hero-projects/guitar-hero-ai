from keys.BaseKey import BaseKey
from keys.HSV import HSV
from keys.KeyBound import KeyBound
from keys.KeyLocation import KeyLocation


class OrangeKey(BaseKey):
  def __init__(self) -> None:
    super().__init__(KeyBound(720, 890), HSV(19, 168, 60), HSV(45, 255, 255), 't')
