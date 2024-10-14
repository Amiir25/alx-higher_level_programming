#!/usr/bin/python3

"""
6-base_geometry.py

This module provides a class with a method that
raises an exception
"""


class BaseGeometry:
    """Contains a method that rasies an exception"""

    def area(self):
        """Raises an exception when called"""

        raise Exception("area() is not implemented")
