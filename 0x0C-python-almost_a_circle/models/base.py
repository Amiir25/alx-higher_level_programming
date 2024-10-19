#!/usr/bin/python3

"""
base.py

This module provides a class 'Base' which used as a base of
all other classes in the project 'Python Almost a Circle'.
"""


class Base:
    """Manages the id attribute"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiates 'id' public instance attribute with the argument id value.
        If 'id' is None, it incerements the '__nb_objects' private class attribute
        and assignes it to 'id'

        Args:
            id (int): the id value
        """

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
