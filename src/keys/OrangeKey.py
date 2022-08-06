from keys.BaseKey import BaseKey
from keys.RGB import RGB
from keys.KeyBound import KeyBound


class OrangeKey(BaseKey):
  def __init__(self) -> None:
    super().__init__(KeyBound(720, 890), RGB(199, 145, 0), RGB(255, 178, 28), 't', 'orange')
