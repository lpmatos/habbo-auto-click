# -*- coding: utf-8 -*-

"""Documentation file axes.py."""

# ==============================================================================
# IMPORTS
# ==============================================================================

from typing import NoReturn, Tuple
from dataclasses import dataclass, field

# ==============================================================================
# CLASS AXES
# ==============================================================================

@dataclass(init=True, repr=True)
class Axes:
  _x: int = field(repr=True, default=0)
  _y: int = field(repr=True, default=0)

  def serialize(self) -> Tuple:
    """
    Return a tuple with X and Y coordinates.
    """
    return (self.x, self.y)

  @property
  def x(self) -> int:
    """
    Return X coordinate.
    """
    return self._x

  @property
  def y(self) -> int:
    """
    Return Y coordinate.
    """
    return self._y
