# -*- coding: utf-8 -*-

"""Documentation file main.py."""

# ==============================================================================
# IMPORTS
# ==============================================================================

import keyboard
import pyautogui, sys
from actions.click import ClickLocation

from settings.log import Log
from settings.arguments import Arguments

import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

# ==============================================================================
# MAIN
# ==============================================================================

if __name__ == "__main__":

  cprint(figlet_format("Auto-Click", font="starwars"), "red", "on_yellow", attrs=["dark"])

  args = Arguments(description="Habbo Auto Click").args

  log_path = args["log_path"] if args["log_path"] else "/log/info"
  log_file = args["log_file"] if args["log_file"] else "file.log"
  delay = float(args["delay"] if args["delay"] else 5.0)

  logger = Log(log_path, log_file, "INFO", "Habbo Auto Click Logger").logger
  print()
  logger.info("Press Ctrl-C to quit.")

  position = ClickLocation(logger).get_click_location()[0]

  try:
    while(True):
      x, y = position[0], position[1]
      logger.info(f"Mouse Position: {position}")
      logger.info(f"Eixo X: {x}")
      logger.info(f"Eixo Y: {y}")
      logger.info(f"Call click with {delay} delay and in {x} - {y}...")
      pyautogui.click(button="left", clicks=5, interval=delay, x=x, y=y)
      sys.stdout.flush()
  except KeyboardInterrupt:
    logger.error(f"Keyboard Error")
  except Exception as error:
    logger.error(f"General Error - {error}")
