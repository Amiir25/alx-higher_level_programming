#!/usr/bin/python3

"""
0-square.py

This module provides a class called Square that defines
a square by private instance attribute 'size'
"""


class Square:
    """
    The Square class defines a square by private instance
    attribute 'size'
    """

    def __init__(self, size=0):
        self.__size = size

    def set_size(self, size):
        """
        Modify the value of 'size'

        Args:
            size (integer): the size of a square

        Return:
            Nothing

        Raises:
            TypeError: if the input is not an integer
            ValueError: if the input is less than 0
        """

        if size > 0:
            try:
                self.__size = size

            except TypeError:
                print("size must be an integer")

            except ValueError:
                print("size must be >= 0")
