#!/usr/bin/python3

"""
rectangle.py

This module provides a class 'Rectangle' that inherits the 'Base'
class of 'base.py' module.
"""

from models.base import Base


class Rectangle(Base):
    """Inherits the 'Base' classof 'base.py' module"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiates four private instance attributes

        Args:
            width (int): must be > 0
            height (int): must be > 0
            x (int): must be >= 0
            y (int): must be >= 0
        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for the private __width attribute"""

        return self.__width

    @width.setter
    def width(self):
        """setter for the private __width attribute"""

        pass

    @property
    def height(self):
        """getter for the private __height attribute"""

        return self.__height

    @height.setter
    def heigh(self):
        """setter for the private __height attribute"""

        pass

    @property
    def x(self):
        """getter for the private __x attribute"""

        return self.__x

    @x.setter
    def x(self):
        """getter for the private __x attribute"""

        pass

    @property
    def y(self):
        """getter for the private __y attribute"""

        return self.__y

    @y.setter
    def y(self):
        """getter for the private __y attribute"""

        pass
