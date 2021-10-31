#!/usr/local/bin/python3.8
# -*- coding: iso-8859-1 -*-

"""
BinaryCalculator.py: This script visualizes the calculative process by logging the important steps and presenting the
final result in the end.
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
from typing import Final, Dict

import tools
from CalculatingUnit import CalculatingUnit
from FullAdder import FullAdder


class BinaryCalculator(tk.Frame):
    """
    This class extends a tkinter Frame to draw a UI for the calculative process and several controls.
    """

    MODE_ADDITION: Final[int] = 0
    MODE_MULTIPLICATION: Final[int] = 1

    WINDOW_TITLE: Final[str] = "Rechner | Binary Calculator"
    WINDOW_GEOMETRY: Final[str] = "800x500"

    COLORS_BTN_NEXT: Final[Dict[str, str]] = {tk.ACTIVE: "#17a589", tk.DISABLED: "#99a3a4"}

    TXT_HEADER: Final[str] = "Berechnet wird {} {} {}..."
    TXT_STEP_LOG: Final[str] = "--> S = {}, C_OUT = {}"
    TXT_Result: Final[str] = "{} {} {} = {}"

    result: str = ""

    def __init__(self, mode: int, value_a: str, value_b: str, master=None):
        if master is not None:
            master.title(self.WINDOW_TITLE)
            master.geometry(self.WINDOW_GEOMETRY)
        super(BinaryCalculator, self).__init__(master)

        self.value_a, self.value_b = tools.fill_up_with_zeros(value_a, value_b)

        if mode == self.MODE_ADDITION:
            self.calculating_unit: CalculatingUnit = FullAdder(self.value_a, self.value_b)

        self.mode = mode

        self.master = master
        self.pack()

        self.font_header = tkf.Font(family="sans-serif", size=25)
        self.font_text = tkf.Font(family="sans-serif", size=18)

        self.lbl_header = tk.Label(self, text=self.TXT_HEADER.format(value_a, self.get_str_operator(mode), value_b),
                                   font=self.font_header)

        self.frm_calc_steps: tk.Frame = tk.Frame(self)
        self.scrollbar: tk.Scrollbar = tk.Scrollbar(self.frm_calc_steps)
        self.listbox_steps: tk.Listbox = tk.Listbox(self.frm_calc_steps, yscrollcommand=self.scrollbar.set,
                                                    font=self.font_text)

        self.listbox_steps.insert(tk.END, self.calculating_unit.get_output_str())

        self.frm_calc_ctrl: tk.Frame = tk.Frame(self)
        self.no_stop: tk.IntVar = tk.IntVar(self)
        self.cbtn_no_stop: tk.Checkbutton = tk.Checkbutton(self.frm_calc_ctrl, text="Nicht pausieren",
                                                           variable=self.no_stop)
        self.btn_next_step: tk.Button = tk.Button(self.frm_calc_ctrl, text="ausführen", command=self.do_next_step,
                                                  bg=self.COLORS_BTN_NEXT[tk.ACTIVE])

        self.lbl_result_binary: tk.Label = tk.Label(self, font=self.font_text)
        self.lbl_result_decimal: tk.Label = tk.Label(self, font=self.font_text)

        self.lbl_header.pack()

        self.frm_calc_steps.pack()
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox_steps.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar.config(command=self.listbox_steps.yview)

        self.frm_calc_ctrl.pack()
        self.cbtn_no_stop.pack(side=tk.LEFT)
        self.btn_next_step.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.lbl_result_binary.pack()
        self.lbl_result_decimal.pack()

    def get_str_operator(self, mode: int) -> str:
        """
        This methode returns the fitting arithmetic operator to the current task.

        :param mode: int
        :return: str
        """
        if mode == self.MODE_ADDITION:
            return "+"
        elif mode == self.MODE_MULTIPLICATION:
            return "*"
        else:
            return "?"

    def do_next_step(self):
        """
        This methode interact with the FullAdder-class to perform the next calculation step.

        :return: None
        """
        self.btn_next_step['state'] = tk.DISABLED
        self.btn_next_step['bg'] = self.COLORS_BTN_NEXT[tk.DISABLED]

        self.calculating_unit.prepare_input()

        result: Final[Dict[int, int]] = self.calculating_unit.read_output()
        self.result = str(result[CalculatingUnit.KEY_RESULT]) + self.result

        print(result)
        print(self.result)

        self.listbox_steps.insert(tk.END, self.TXT_STEP_LOG.format(result[CalculatingUnit.KEY_RESULT],
                                                                   result[CalculatingUnit.KEY_C]))

        self.listbox_steps.insert(tk.END, self.calculating_unit.get_output_str())

        if not self.calculating_unit.is_calc_finished():
            self.btn_next_step['bg'] = self.COLORS_BTN_NEXT[tk.ACTIVE]
            self.btn_next_step['state'] = tk.ACTIVE

            if self.no_stop.get() == 1:
                self.do_next_step()

        else:
            self.calculating_unit.cleanup()
            self.lbl_result_binary['text'] = self.TXT_Result.format(self.value_a, tools.get_operator_sign(self.mode),
                                                                    self.value_b, self.result)
            self.lbl_result_decimal['text'] = self.TXT_Result.format(tools.binary_to_decimal(self.value_a),
                                                                     tools.get_operator_sign(self.mode),
                                                                     tools.binary_to_decimal(self.value_b),
                                                                     tools.binary_to_decimal(self.result))
