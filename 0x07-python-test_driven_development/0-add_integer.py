#!/usr/bin/python3
"""
    This module provides a function that adds two numbers.
    The numbers can be either integers or floats. Floats
    can be coverted into integers.
"""


def add_integer(a, b=98):

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testfile("0-add_integer.txt")
