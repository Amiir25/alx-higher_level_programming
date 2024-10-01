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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
