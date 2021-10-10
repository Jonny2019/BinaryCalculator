# -*- coding: iso-8859-1 -*-

"""
FullAdder.py: This script handles the interaction with the hardware to carryout a binary addition of two inputs.
"""

__author__ = "Justus Bendel"
__copyright__ = "Copyright 2021, Justus Bendel"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Justus Bendel"
__email__ = "justus.bendel@live.de"
__status__ = "Development"

from typing import List, Dict, Final

from CalculatingUnit import CalculatingUnit
from tools import overrides


class FullAdder(CalculatingUnit):
    """
    This class controls a hardware-side Full Adder and carries out single operation for every digit pair in order to
    provide the result in the end.
    """

    PIN_A: Final[int] = 7       # GPIO7 <-> physical: GPIO4
    PIN_B: Final[int] = 11      # GPIO0 <-> physical: GPIO17
    PIN_C_IN: Final[int] = 13   # GPIO2 <-> physical: GPIO27
    PIN_C_OUT: Final[int] = 15  # GPIO3 <-> physical: GPIO22

    TXT_OUTPUT: Final[str] = "Eingabe: A={}, B={}, C={}"

    digit_pointer: int = 0
    current_carryover: int = 0

    def __init__(self, value_a: str, value_b: str):
        self.value_a: Final[str] = value_a
        self.value_b: Final[str] = value_b

        self.digits_a: Final[List[int]] = self.get_int_list(self.value_a)
        self.digits_b: Final[List[int]] = self.get_int_list(self.value_b)

    @overrides(CalculatingUnit)
    def prepare_input(self, params: Dict[int, int]) -> bool:
        print("input has been prepared with params " + str(params))
        return True

    @overrides(CalculatingUnit)
    def read_output(self) -> Dict[int, int]:
        print("output has been read")
        return {CalculatingUnit.KEY_RESULT: 1, CalculatingUnit.KEY_C: 0}

    @overrides(CalculatingUnit)
    def get_output_str(self) -> str:
        return self.TXT_OUTPUT.format(self.digits_a[self.digit_pointer], self.digits_b[self.digit_pointer],
                                      self.current_carryover)

    @staticmethod
    def get_int_list(s: str) -> List[int]:
        """
        This methode returns a list of integer values from a string.

        :param s: input string: str
        :return: list of digits: List[int]
        """
        return list(map(lambda x: int(x), list(s)))
