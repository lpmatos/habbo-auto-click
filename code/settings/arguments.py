
# -*- coding: utf-8 -*-

"""Documentation file arguments.py."""

# ==============================================================================
# IMPORTS
# ==============================================================================

import argparse
from typing import NoReturn, Text
from settings.exception import CreateParserException

# ==============================================================================
# CLASS - ARGUMENTS
# ==============================================================================

class Arguments:

  def __init__(self, *args, **kwargs) -> NoReturn:
    self._parser = self._create_parser_object(*args, **kwargs)
    self._adding_arguments()
    self.args = vars(self._parser.parse_args())

  @staticmethod
  def _create_parser_object(*args, **kwargs) -> argparse.ArgumentParser:
    try:
      return argparse.ArgumentParser(*args, **kwargs)
    except argparse.ArgumentError as error:
      print(f"Error when we create a parser object - {error}")
    except CreateParserException as error:
      print(f"Error general exception in create a parser object - {error}")

  def _adding_arguments(self) -> NoReturn:
    self._parser.add_argument("-d", "--delay",
                                type=float,
                                metavar="<delay>",
                                default=3.0,
                                help="Delay")
    self._parser.add_argument("-log_path", "--log_path",
                                type=str,
                                metavar="<log-path>",
                                default=None,
                                help="Log Path name")
    self._parser.add_argument("-log_file", "--log_file",
                                type=str,
                                metavar="<log-file>",
                                default=None,
                                help="Log File name")
