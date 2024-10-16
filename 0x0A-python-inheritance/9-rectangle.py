#!/usr/bin/python3

"""
9-rectangle.py

This module provides a class 'Rectangle' that inherits
the class 'BaseGeometry' and calculates the area of a
rectangle
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
