#!/usr/bin/python3

"""
4-inheits_from.py

This module provides a function that checks if an
object is an instance of a class that inherited
(directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True an object is an instance a class that inherited
    (directly or indirectly) from the specified class, otherwise False.
    """

    return isinstance(obj, a_class) and not type(obj) is a_class
