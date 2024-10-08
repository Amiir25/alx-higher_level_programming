#!/usr/bin/python3
"""
101-locked_class.py

This module provides a class that prevents the user from
dynamically creating new instance attributes except for
'first_name'
"""


class LockedClass:
    """
    A class to prevent the user from creating new instance attribute
    that is not 'first_name'
    """

    __slots__ = 'first_name'
