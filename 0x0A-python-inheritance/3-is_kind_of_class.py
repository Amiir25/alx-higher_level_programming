#!/usr/bin/python3

"""
2-is_kind_of_class.py

This module provides a function that checks if an
object is an instance a paret or child class.
"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class"""

    return isinstance(obj, a_class)
