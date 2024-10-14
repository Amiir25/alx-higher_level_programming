#!/usr/bin/python3

"""
2-is_same_class.py

This module provides a function that checks if an
object is an instance a class.
"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a class"""

    return isinstance(obj, a_class) and type(obj) is a_class
