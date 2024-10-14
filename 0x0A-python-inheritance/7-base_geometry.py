#!/usr/bin/python3

"""
7-base_geometry.py

This module provides a class with a method that
raises an exception and a method that validates
a value.
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
