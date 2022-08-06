from keys.BaseKey import BaseKey
from keys.RGB import RGB
from keys.KeyBound import KeyBound


class YellowKey(BaseKey):
  def __init__(self) -> None:
    super().__init__(KeyBound(360, 530), RGB(225, 225, 0), RGB(255, 255, 20), 'e', 'yellow')
