#!/usr/local/bin/python3.8
# -*- coding: iso-8859-1 -*-

"""
Home.py: This script provides a graphical interface for a more user-friendly handling of the calculative functions.
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
from typing import Final, List

from BinaryCalculator import BinaryCalculator
from tools import binary_to_decimal, decimal_to_binary

title_win: Final[str] = "Home | Binary Calculator"
geometry_win: Final[str] = "800x500"


class Home(tk.Frame):
    """
    This class extends a tkinter Frame widget to hold all other necessary widgets in it.
    """

    options_link: Final[List[List[any]]] = [["Addition", BinaryCalculator.MODE_ADDITION, "+"],
                                            ["Multiplikation", BinaryCalculator.MODE_MULTIPLICATION, "*"]]
    options: Final[List[str]] = list(map(lambda opt: opt[0], options_link))

    def __init__(self, master=None):
        super(Home, self).__init__(master)

        self.master = master
        self.pack()

        self.font_header = tkf.Font(family="sans-serif", size=25)
        self.font_text = tkf.Font(family="sans-serif", size=18)

        self.lbl_mode = tk.Label(self, text="Bitte wähle einen Rechenmodus aus:", font=self.font_header)

        self.selected_mode = tk.StringVar(self)
        self.selected_mode.set(self.options[0])

        self.mode_menu = tk.OptionMenu(self, self.selected_mode, *self.options, command=self.selection_changed)
        self.mode_menu.config(font=self.font_text)

        self.frame_input = tk.Frame(self)

        self.frame_a = tk.Frame(self.frame_input)
        self.lbl_header_binary = tk.Label(self.frame_a, text='binär', font=self.font_text)
        self.lbl_header_decimal = tk.Label(self.frame_a, text='dezimal', font=self.font_text)
        self.var_a_b = tk.StringVar(value='0')
        self.var_a_b.trace_add("write", self.translate_ab_to_ad)
        self.input_a_b = tk.Entry(self.frame_a, textvariable=self.var_a_b, font=self.font_text)
        self.var_a_d = tk.StringVar(value='0')
        self.var_a_d.trace_add("write", self.translate_ad_to_ab)
        self.input_a_d = tk.Entry(self.frame_a, textvariable=self.var_a_d, font=self.font_text)

        self.lbl_operator = tk.Label(self.frame_input, text=self.options_link[0][2], font=self.font_text)

        self.frame_b = tk.Frame(self.frame_input)
        self.var_b_b = tk.StringVar(value='0')
        self.var_b_b.trace_add("write", self.translate_bb_to_bd)
        self.input_b_b = tk.Entry(self.frame_b, textvariable=self.var_b_b, font=self.font_text)
        self.var_b_d = tk.StringVar(value='0')
        self.var_b_d.trace_add("write", self.translate_bd_to_bb)
        self.input_b_d = tk.Entry(self.frame_b, textvariable=self.var_b_d, font=self.font_text)

        self.btn_calculate = tk.Button(self, text='=', font=self.font_header, bg='#17a589', command=self.start_calc)

        self.lbl_mode.pack()
        self.mode_menu.pack(pady=20)

        self.frame_input.pack()

        self.frame_a.pack()
        self.lbl_header_binary.grid(row=1, column=1, pady=20)
        self.lbl_header_decimal.grid(row=1, column=2, pady=20)
        self.input_a_b.grid(row=2, column=1, padx=10)
        self.input_a_d.grid(row=2, column=2, padx=10)

        self.lbl_operator.pack(pady=20)

        self.frame_b.pack()
        self.input_b_b.grid(row=1, column=1, padx=10)
        self.input_b_d.grid(row=1, column=2, padx=10)

        self.btn_calculate.pack(pady=20)

    def selection_changed(self, *args):
        mode_name: Final[str] = self.selected_mode.get()

        for opt in self.options_link:
            if opt[0] == mode_name:
                self.lbl_operator['text'] = opt[2]
                break

    def start_calc(self, *args):
        a_b: Final[str] = self.var_a_b.get()
        b_b: Final[str] = self.var_b_b.get()

        mode_name: Final[int] = self.selected_mode.get()
        mode: [int] = None
        for opt in self.options_link:
            if opt[0] == mode_name:
                mode = opt[1]
                break

        win = tk.Tk()
        binary_calculator: BinaryCalculator = BinaryCalculator(mode, a_b, b_b, master=win)
        binary_calculator.mainloop()

    def translate_ab_to_ad(self, *args):
        """
        This methode is used to react to a change of a user input by mirroring the decimal representation of it to the
        right Entry.

        :return: None
        """
        self.var_a_d.set(str(binary_to_decimal(str(self.var_a_b.get()))))

    def translate_ad_to_ab(self, *args):
        """
        This methode is used to react to a change of a user input by mirroring the binary representation of it to the
        right Entry.

        :return: None
        """
        try:
            self.var_a_b.set(str(decimal_to_binary(int(self.var_a_d.get()))))
        except ValueError as e:
            self.var_a_b.set('0')
            print(e)

    def translate_bb_to_bd(self, *args):
        """
        This methode is used to react to a change of a user input by mirroring the decimal representation of it to the
        right Entry.

        :return: None
        """
        self.var_b_d.set(str(binary_to_decimal(str(self.var_b_b.get()))))

    def translate_bd_to_bb(self, *args):
        """
        This methode is used to react to a change of a user input by mirroring the binary representation of it to the
        right Entry.

        :return: None
        """
        try:
            self.var_b_b.set(str(decimal_to_binary(int(self.var_b_d.get()))))
        except ValueError as e:
            self.var_b_b.set('0')
            print(e)


if __name__ == "__main__":
    root = tk.Tk()
    root.title(title_win)
    root.geometry(geometry_win)
    window = Home(master=root)
    window.mainloop()
