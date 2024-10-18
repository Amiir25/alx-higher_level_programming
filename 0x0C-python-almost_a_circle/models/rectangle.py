#!/usr/bin/python3

"""
rectangle.py

This module provides a class 'Rectangle' that inherits the 'Base'
class of 'base.py' module.
"""

from models.base import Base


class Rectangle(Base):
    """Inherits the 'Base' class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiates four private instance attributes

        Args:
            width (int)
            height (int)
            x (int)
            y (int)
        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.y = y
        super().__init__(id)
