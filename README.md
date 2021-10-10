# BinaryCalculator

This Python-based program is designed to run on a Raspberry Pi (2) with Python version above 3.8.5.
It's purpose is to controle a hardware attached binary Full Adder by GPIO-Pins and performe simple addition and multiplication tasks.
Over all this project was developed in the context of a presentation on binary calculation.

## Program structure
This paragraph contains a brife summary of each file of the project.

### Home.py
This script provides a graphical interface for a more user-friendly handling of the calculative functions.
The GUI is designed to handle user inputs of the values used in the calculation.
An automatical conversion on binary and decimal inputs is provided as well in both directions.

### BinaryCalculator.py
This script provides a graphical interface for the output and controle of the calculation process to make it more understandable for the user (audience).

### CalculatingUnit.py
This script offers a blueprint for a class dealing with a binary calculation. It provides an (abstract) class which has to be extended by every class which handles a type of binary calculation.

### FullAdder.py
This script handles the interaction with the hardware to carryout a binary addition of two inputs. It mainly contains a class which controls a hardware-side Full Adder and carries out single operation for every digit pair in order toprovide the result in the end.

### tools.py
A collection of functions which are mainly used for linting, debugging and extraction of commonly used functions.

## Hardware implementation
