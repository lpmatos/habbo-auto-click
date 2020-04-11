# -*- coding: utf-8 -*-

"""Documentation file click.py."""

# ==============================================================================
# IMPORTS
# ==============================================================================

from typing import NoReturn, Tuple
from utils.coordinates import Coordinates

# ==============================================================================
# CLASS CLICK
# ==============================================================================

class Click(Coordinates):

  def __init__(self, original: Tuple) -> NoReturn:
    super().__init__(original)
    self.current = original
