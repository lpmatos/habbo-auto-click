# -*- coding: utf-8 -*-

"""Documentation file coordinates.py."""

# ==============================================================================
# IMPORTS
# ==============================================================================

from utils.axes import Axes
from dataclasses import dataclass, field
from typing import NoReturn, List, Tuple

# ==============================================================================
# CLASS COORDINATES
# ==============================================================================

@dataclass(init=True, repr=True)
class Coordinates:

  def __init__(self, original: Tuple) -> NoReturn:
    self._original = Axes(original[0], original[1]).serialize()
    self._current = Axes(0, 0).serialize()

  def serialize(self) -> List:
    """
    Return a list with original and current coordinates.
    """
    return [tuple(self.original), tuple(self.current)]

  @property
  def original(self) -> Tuple:
    """
    Return the original coordinate.
    """
    return self._original

  @property
  def current(self) -> Tuple:
    """
    Return the current coordinate.
    """
    return self._current

  @current.setter
  def current(self, current):
    self._current = current
