# dice.py
# a simple Python object which simulates a playing die.
# author: pcostjr
# created: 1.23.2025
# last update: 1.23.2025

import random

class Die:
    def __init__(self):
        # amount of faces on this die
        self.faces = 6
        # current value of the die. Default is -1 to indicate unrolled
        self.value = -1

    def roll(self):
        self.value = random.randint(1, self.faces)

    # return the last rolled value of the die
    def get_value(self):
        return self.value

    def __str__(self):
        if self.value == -1:
            return "This die hasn't been rolled yet..."
        return f"This die currently reads {self.value}"
        # return "This die hasn't been rolled yet..." if self.value == -1 else f"This die currently reads {self.value}"