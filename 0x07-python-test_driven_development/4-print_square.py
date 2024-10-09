#!/usr/bin/python3
"""
    This code provides a function that prints a square
    with the character #.
"""


def print_square(size=None):
    """
    This function prints a square with the
    character #

    Args:
        size (int): the size of the square

    Raises:
        TypeError: if size is not integer
        ValueError: if size < 0
    """

    if size is None:
        raise TypeError("size must be an integer")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", sep='', end='')

        print()


if __name__ == "__main__":
    import doctest
    doctest.testfile("4-print_square.txt")
