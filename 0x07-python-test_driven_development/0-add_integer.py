#!/usr/bin/python3
"""
    This module provides a function that adds two numbers.
    The numbers can be either integers or floats. Floats
    can be coverted into integers.
"""


def add_integer(a, b=98):
    """
    Adds two numbers

    Args:
        a: the first number (int or float)
        b: the second number (int or float) default = 98

    Raises:
        TypeError: if a or b are not integers or floats
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    # checking for NaN and infinity
    if isinstance(a, float) and (
        a != a or a == float("inf") or a == -float("inf")
    ):
        raise ValueError("can not convert float NaN to integer")

    if isinstance(b, float) and (
        b != b or b == float('inf') or b == -float('inf')
    ):
        raise ValueError("cannot convert float NaN to integer")

    a = int(a)
    b = int(b)

    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testfile("0-add_integer.txt")
