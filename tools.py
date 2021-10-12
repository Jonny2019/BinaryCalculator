# -*- coding: iso-8859-1 -*-

"""
tools.py: A collection of functions which are used for linting and debugging.
"""

__author__ = "Justus Bendel"
__copyright__ = "Copyright 2021, Justus Bendel"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Justus Bendel"
__email__ = "justus.bendel@live.de"
__status__ = "Production"

from typing import Final, List, Tuple


def overrides(interface_class):
    """
    Function override annotation.
    Corollary to @abc.abstractmethod where the override is not of an
    abstractmethod.
    Modified from answer https://stackoverflow.com/a/8313042/471376
    """

    def confirm_override(method):
        if method.__name__ not in dir(interface_class):
            raise NotImplementedError('function "%s" is an @override but that'
                                      ' function is not implemented in base'
                                      ' class %s'
                                      % (method.__name__,
                                         interface_class)
                                      )

        def func():
            pass

        attr = getattr(interface_class, method.__name__)
        if type(attr) is not type(func):
            raise NotImplementedError('function "%s" is an @override'
                                      ' but that is implemented as type %s'
                                      ' in base class %s, expected implemented'
                                      ' type %s'
                                      % (method.__name__,
                                         type(attr),
                                         interface_class,
                                         type(func))
                                      )
        return method

    return confirm_override


def binary_to_decimal(b: str) -> int:
    """
    This methode converts a given binary string into it's decimal representation and returns it or 0 in case of an
    unsupported input.

    :param b: str
    :return: int
    """
    prefix_binary: Final[str] = '0b{}'
    d: int = 0
    try:
        d = int(prefix_binary.format(b), 2)
    except ValueError as e:
        print(e)
    return d


def decimal_to_binary(d: int) -> str:
    """
    This methode converts a given decimal number into it's binary representation and returns it or 0 in case of an
    unsupported input.

    :param d: int
    :return: str
    """
    b: str = '0'
    try:
        b = bin(d).replace('0b', '')
    except ValueError as e:
        print(e)
    return b


def fill_up_with_zeros(v1: str, v2: str) -> Tuple[str, str]:
    if len(v1) == len(v2):
        print("even")
        return v1, v2
    elif len(v1) > len(v2):
        print("v1 > v2")
        l2: List[str] = list(v2)
        for i in range(0, len(v1) - len(v2)):
            l2.insert(0, "0")
            print(l2)
        return v1, list_to_str(l2)
    elif len(v1) < len(v2):
        print("v1 < v2")
        l1: List[str] = list(v1)
        for i in range(0, len(v2) - len(v1)):
            l1.insert(0, "0")
        return list_to_str(l1), v2


def list_to_str(lst: List) -> str:
    s: str = ""
    for i in lst:
        s += i
    return s
