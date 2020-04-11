# -*- coding: utf-8 -*-

"""Documentation file os.py."""

# =============================================================================
# IMPORTS
# =============================================================================

from typing import NoReturn, Callable
from constants.message import NOT_WINDOWS

try:
  from win10toast import ToastNotifier
except Exception as error:
  print(NOT_WINDOWS)

# =============================================================================
# CLASS - TOAST
# =============================================================================

class Toast:

  def __init__(self, logger: Callable) -> NoReturn:
    self._logger = logger
    self.toaster = ToastNotifier()

  def notification(self, title, message, *args, **kwargs) -> NoReturn:
    try:
      self.toaster.show_toast(title, message, duration=2, *args, **kwargs)
    except Exception as error:
      self.logger.error(f"Notification Exception = {error}")

  @property
  def logger(self) -> Callable:
    return self._logger
