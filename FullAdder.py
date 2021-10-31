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

import RPi.GPIO as gpio
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
    PIN_S: Final[int] = 29      # GPIO21<-> physical: GPIO5

    TXT_OUTPUT: Final[str] = "Eingabe: A={}, B={}, C={}"

    digit_pointer: int = 0
    current_carryover: int = 0

    def __init__(self, value_a: str, value_b: str):
        self.value_a: Final[str] = value_a
        self.value_b: Final[str] = value_b

        self.digits_a: Final[List[int]] = self.get_int_list(self.value_a)
        self.digits_b: Final[List[int]] = self.get_int_list(self.value_b)
        self.digits_a.reverse()
        self.digits_b.reverse()

        gpio.setmode(gpio.BOARD)
        gpio.setup(self.PIN_A, gpio.OUT)
        gpio.setup(self.PIN_B, gpio.OUT)
        gpio.setup(self.PIN_C_IN, gpio.OUT)
        gpio.setup(self.PIN_C_OUT, gpio.IN)
        gpio.setup(self.PIN_S, gpio.IN)

    @overrides(CalculatingUnit)
    def prepare_input(self) -> bool:
        if self.digits_a[self.digit_pointer] == 1:
            gpio.output(self.PIN_A, gpio.HIGH)
        if self.digits_b[self.digit_pointer] == 1:
            gpio.output(self.PIN_B, gpio.HIGH)
        if self.current_carryover == 1:
            gpio.output(self.PIN_C_IN, gpio.HIGH)
        return True

    @overrides(CalculatingUnit)
    def read_output(self) -> Dict[int, int]:
        print("output has been read")
        self.current_carryover = gpio.input(self.PIN_C_OUT)
        self.digit_pointer += 1
        return {CalculatingUnit.KEY_RESULT: gpio.input(self.PIN_S), CalculatingUnit.KEY_C: gpio.input(self.PIN_C_OUT)}

    @overrides(CalculatingUnit)
    def get_output_str(self) -> str:
        return self.TXT_OUTPUT.format(self.digits_a[self.digit_pointer], self.digits_b[self.digit_pointer],
                                      self.current_carryover)

    def clear_input(self) -> None:
        """
        This methode sets all outputs to 0.

        :return: None
        """
        gpio.output(self.PIN_A, gpio.LOW)
        gpio.output(self.PIN_B, gpio.LOW)
        gpio.output(self.PIN_C_IN, gpio.LOW)

    @overrides(CalculatingUnit)
    def is_calc_finished(self) -> bool:
        return self.digit_pointer + 1 == len(self.digits_a)

    @overrides(CalculatingUnit)
    def cleanup(self) -> None:
        gpio.cleanup()

    @staticmethod
    def get_int_list(s: str) -> List[int]:
        """
        This methode returns a list of integer values from a string.

        :param s: input string: str
        :return: list of digits: List[int]
        """
        return list(map(lambda x: int(x), list(s)))
