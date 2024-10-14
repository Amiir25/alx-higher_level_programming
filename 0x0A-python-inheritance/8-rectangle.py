#!/usr/bin/python3

"""
8-rectangle.py

This module provides a class 'Rectangle' that inherits
from class 'BaseGeometry' and instatiates private attributes
'width' and 'height'.
"""


class BaseGeometry:
    """Contains a method that rasies an exception"""

    def area(self):
        """Raises an exception when called"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""

        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Inherits from 'BaseGeometry' and instantiates private attributes"""

    def __init__(self, width, height):
        """Instantiates width and height"""

        self.integer_validator("width", height)
        self.integer_validator("height", width)

        self.__width = width
        self.__height = height
