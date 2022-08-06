from keys.BaseKey import BaseKey
from keys.KeyBound import KeyBound
from keys.RGB import RGB


class BlueKey(BaseKey):
  def __init__(self) -> None:
    super().__init__(KeyBound(540, 710), RGB(0, 118, 203), RGB(50, 139, 255), 'r', 'blue')
