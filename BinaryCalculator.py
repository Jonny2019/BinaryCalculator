#!/usr/local/bin/python3.8
# -*- coding: iso-8859-1 -*-

"""
BinaryCalculator.py: This script
"""

__author__ = "Justus Bendel"
__copyright__ = "Copyright 2021, Justus Bendel"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Justus Bendel"
__email__ = "justus.bendel@live.de"
__status__ = "Development"

import tkinter as tk
import tkinter.font as tkf
from typing import Final

from CalculatingUnit import CalculatingUnit
from FullAdder import FullAdder


class BinaryCalculator(tk.Frame):
    MODE_ADDITION: Final[int] = 0
    MODE_MULTIPLICATION: Final[int] = 1

    WINDOW_TITLE: Final[str] = "Rechner | Binary Calculator"
    WINDOW_GEOMETRY: Final[str] = "800x500"

    TXT_HEADER: Final[str] = "Berechnet wird {} {} {}..."

    def __init__(self, mode: int, value_a: str, value_b: str, master=None):
        if master is not None:
            master.title(self.WINDOW_TITLE)
            master.geometry(self.WINDOW_GEOMETRY)
        super(BinaryCalculator, self).__init__(master)

        self.master = master
        self.pack()

        self.font_header = tkf.Font(family="sans-serif", size=25)
        self.font_text = tkf.Font(family="sans-serif", size=18)

        self.lbl_header = tk.Label(self, text=self.TXT_HEADER.format(value_a, self.get_str_operator(mode), value_b),
                                   font=self.font_header)

        self.frm_calc_steps: tk.Frame = tk.Frame(self)
        self.scrollbar: tk.Scrollbar = tk.Scrollbar(self.frm_calc_steps)
        self.listbox_steps: tk.Listbox = tk.Listbox(self.frm_calc_steps, yscrollcommand=self.scrollbar.set)

        for i in range(0, 20):
            self.listbox_steps.insert(tk.END, "This is line number " + str(i))

        self.lbl_header.pack()

        self.frm_calc_steps.pack()
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox_steps.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar.config(command=self.listbox_steps.yview)

        if mode == self.MODE_ADDITION:
            self.calculating_unit: CalculatingUnit = FullAdder(value_a, value_b)

    def get_str_operator(self, mode: int) -> str:
        if mode == self.MODE_ADDITION:
            return "+"
        elif mode == self.MODE_MULTIPLICATION:
            return "*"
        else:
            return "?"
