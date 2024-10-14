#!/usr/bin/python3

"""
0-lookup.py

This module provides a function that returns a list
of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the available attributes and methods of an object using
    the dir() built-in function.
    """

    return dir(obj)
