#!/usr/bin/python3

"""
2-is_kind_of_class.py

This module provides a function that checks if an
object is an instance a specified class or an instance
of any class that inherits from the specified class.
"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class or its child classes"""

    return isinstance(obj, a_class)
