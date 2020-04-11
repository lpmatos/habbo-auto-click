# -*- coding: utf-8 -*-

"""Documentation file run.py."""

# ==============================================================================
# IMPORTS
# ==============================================================================

import pyautogui, sys

from tools.os import OSystem
from settings.log import Log
from utils.toast import Toast
from actions.click import ClickLocation
from settings.arguments import Arguments

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

from typing import NoReturn, Tuple, Callable

# ==============================================================================
# GLOBAL
# ==============================================================================

os = OSystem()
args = Arguments(description="Habbo Auto Click").args

log_path = args["log_path"] if args["log_path"] else "./log/info"
log_file = args["log_file"] if args["log_file"] else "file.log"
delay = float(args["delay"]) if args["delay"] else 2.0

# ==============================================================================
# FUNCTIONSx
# ==============================================================================

def apply_auto_click(logger: Callable, position: Tuple) -> NoReturn:
  try:
    contador = 1
    while(True):
      x, y = position[0], position[1]
      logger.info(f"Mouse Position: {position}")
      logger.info(f"Eixo X: {x}")
      logger.info(f"Eixo Y: {y}")
      logger.info(f"Call - {contador} click - delay {delay} (s) - Coordinate  X: {x} - Y: {y}...")
      print()
      pyautogui.click(button="left", clicks=5, interval=delay, x=x, y=y)
      contador += 1
      sys.stdout.flush()
  except KeyboardInterrupt:
    logger.error(f"Keyboard Error")
  except Exception as error:
    logger.error(f"General Error when we apply the auto click - {error}")

# ==============================================================================

def run():
  try:
    os.check_system_plataform()
    cprint(figlet_format("Auto-Click", font="starwars"), "red", "on_yellow", attrs=["dark"])
    print()
    logger = Log(log_path, log_file, "INFO", "Habbo Auto Click Logger").logger
    print()
    toast = Toast(logger)
    toast.notification("Hey! The Habbo Auto Click has started.", "💩 Are you ready to start 💩!")
    logger.debug("Press Ctrl-C to quit.")
    logger.info("Getting original location")
    click = ClickLocation(logger)
    position = click.get_click_location()[0]
    apply_auto_click(logger, position)
    toast.notification("Hey! The Habbo Auto Click has ended.", "👋🏻 Bye Bye 👋🏻!")
  except Exception as error:
    logger.error(f"General Error Run - {error}")
