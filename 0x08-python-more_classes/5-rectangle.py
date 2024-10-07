#!/usr/bin/python3
"""
3- rectangle.py

This module provides a class Rectangle that defines
a rectangle by width and height and calculates the
area and perimeter of a rectangle. It finally prints
the rectangle with # sign.
"""


class Rectangle:
    """
    This class defines a rectangle, calculates the area and perimeter of a
    rectangle and prints the rectangle with # sign
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle, or
        empty string if either width or height are 0.
        """

        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect_str += "#"
            if i < self.__height - 1:
                rect_str += "\n"

        return rect_str

    def __repr__(self):
        """
        Returns a dtring representation of the rectangle that
        can be used to recreate a new instance
        """

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message when an instance of the rectangle
        is removed
        """

        print("Bye rectangle...")
