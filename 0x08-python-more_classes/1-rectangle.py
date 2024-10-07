#!/usr/bin/python3
"""
1- rectangle.py

This module provides a class Rectangle that defines
a rectangle by private instance attributes of width
and height.
"""


class Rectangle:
    """
    The Rectangle class defines a rectangle by private
    intstance attributes 'width' and 'height'
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        return self.__width

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

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
