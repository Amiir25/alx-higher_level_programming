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

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if isinstance(position, tuple):
            if all(isinstance(i, int) and i > 0 for i in position):
                self.__position = position

        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        Calculates area

        Returns:
            The area of a square
        """

        return self.__size * self.__size

    def my_print(self):
        """
        Prints a square of # character

        Returns:
            Nothing
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[0]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
