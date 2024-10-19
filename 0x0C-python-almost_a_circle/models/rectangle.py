#!/usr/bin/python3

"""
rectangle.py

This module provides a class 'Rectangle' that inherits the 'Base'
class of 'base.py' module.
"""

from models.base import Base


class Rectangle(Base):
    """Inherits the 'Base' class of 'base.py' module"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiates four private instance attributes

        Args:
            width (int): must be > 0
            height (int): must be > 0
            x (int): must be >= 0
            y (int): must be >= 0
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for the private __width attribute"""

        return self.__width

    @width.setter
    def width(self, width):
        """setter for the private __width attribute"""

        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        """getter for the private __height attribute"""

        return self.__height

    @height.setter
    def height(self, height):
        """setter for the private __height attribute"""

        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @property
    def x(self):
        """getter for the private __x attribute"""

        return self.__x

    @x.setter
    def x(self, x):
        """getter for the private __x attribute"""

        if not isinstance(x, int):
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @property
    def y(self):
        """getter for the private __y attribute"""

        return self.__y

    @y.setter
    def y(self, y):
        """getter for the private __y attribute"""

        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y

    def area(self):
        """Returns the area of the Rectangle"""

        return self.__width * self.__height
