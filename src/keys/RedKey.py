from keys.BaseKey import BaseKey
from keys.RGB import RGB
from keys.KeyBound import KeyBound


class RedKey(BaseKey):
  def __init__(self) -> None:
    super().__init__(KeyBound(180, 350), RGB(205, 0, 0), RGB(255, 28, 29), 'w', 'red')
