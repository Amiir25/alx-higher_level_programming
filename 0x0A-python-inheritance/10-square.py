#!/usr/bin/python3

"""
10-square.py

This module provides a class 'Square' that inherits
the class 'Rectangle' and calculates a square.
"""


class BaseGeometry:
    """Contains a method that rasies an exception"""

    def area(self):
        """Raises an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value

        Args:
            name: the name of the parameter
            value: the value of the parameter

        Raises:
            TypeError: when value is not an integer
            ValueError: when value is <= 0
        """

        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Inherits the class 'BaseGeometry' and instantiates private attributes
    width and height
    """

    def __init__(self, width, height):
        """
        Instantiates width and height

        Args:
            width: the width the rectangle
            height: the height the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of a rectangle"""

        return self.__width * self.__height

        def __str__(self):
            """Returns the string description of the rectangle"""

            return ("Rectangle {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """Inherits the class 'Rectangle' and calculates square"""

    def __init__(self, size):
        """Instantiates size"""

        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """Calculates the square of the size"""

        return self.__size ** 2

        def __str__(self):
            """Returns the string description of the rectangle"""

            return ("Rectangle {}/{}".format(self.__width, self.__height))
