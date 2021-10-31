# -*- coding: iso-8859-1 -*-

"""
CalculatingUnit.py: This script offers a blueprint for a class dealing with a binary calculation.
"""

__author__ = "Justus Bendel"
__copyright__ = "Copyright 2021, Justus Bendel"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Justus Bendel"
__email__ = "justus.bendel@live.de"
__status__ = "Development"

from typing import Dict, Final


class CalculatingUnit(object):
    """
    Abstract class which has to be extended by every class which handles a type of binary calculation.
    """

    KEY_A: Final[int] = 0       # key to the value of the first bit
    KEY_B: Final[int] = 1       # key to the value of the second bit
    KEY_C: Final[int] = 2       # key to the value of the carryover (In/OUT)
    KEY_RESULT: Final[int] = 3  # key to the value of the calculation result

    def prepare_input(self) -> bool:
        """
        This methode is supposed to handle the preparation of a calculation by the experimental setup.

        :return: bool
        """
        pass

    def read_output(self) -> Dict[int, int]:
        """
        This methode is supposed to read out the physical values and to return their logical representation in order to
        the calculative process.

        :return: Dict[int, int]
        """
        pass

    def get_output_str(self) -> str:
        """
        This methode is supposed to return a string which summarizes to current occupation and can be shown to the user.
        :return: str
        """
        pass

    def is_calc_finished(self) -> bool:
        """
        This methode checks weather the calculation has finished or not yet.

        :return: bool
        """
        pass

    def clear_input(self) -> None:
        """
        This methode should sets all outputs to 0.

        :return: None
        """
        pass

    def cleanup(self) -> None:
        """
        This methode should perform necessary cleanup tasks for used GPIOs.

        :return: None
        """
        pass
