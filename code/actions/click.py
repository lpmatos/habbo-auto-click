# -*- coding: utf-8 -*-

"""Documentation file click.py."""

# ==============================================================================
# IMPORTS
# ==============================================================================

import keyboard
import pyautogui
from clients.click import Click
from constants.message import INFO
from typing import NoReturn, Tuple, List, Callable

# ==============================================================================
# CLASS CLICK LOCATION
# ==============================================================================

class ClickLocation:

  def __init__(self, logger: Callable) -> NoReturn:
    self._logger = logger

  def get_click_location(self) -> List:
    try:
      print(INFO)
      keyboard.wait("x")
      self.logger.info(f"Display information: {self.get_screen_size()}")
      self.logger.info("Selected target!")
      print()
      return Click(pyautogui.position()).serialize()
    except KeyboardInterrupt:
      print(f"Keyboard Error")
      return ""

  @staticmethod
  def get_screen_size() -> Tuple:
    return tuple(pyautogui.size())

  @staticmethod
  def get_position() -> Tuple:
    return tuple(pyautogui.position())

  @property
  def logger(self) -> Callable:
    return self._logger
