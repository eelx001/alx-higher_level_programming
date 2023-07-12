#!/usr/bin/python3
"""
Module 100-my_int
Contains class MyInt that inherits from int
Sneaky --> has == and != operators inverted!
"""

"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
