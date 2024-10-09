#!/usr/bin/python3
"""
    This code provides a function that prints a square
    with the character #.
"""


def print_square(size=None):
    """
    This function prints a square with the
    character #
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", sep='', end='')

        print()


if __name__ == "__main__":
    import doctest
    doctest.testfile("4-print_square.txt")
