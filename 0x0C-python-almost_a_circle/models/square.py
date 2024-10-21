#!/usr/bin/python3

"""
square.py

This module provides a 'Square' class that iherits the
'Rectangle' class of 'rectangle.py' module.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits the 'Rectangle' class of 'rectangle.py'"""

    def __init__(slef, size, x=0, y=0, id=None):
        """ """

        super().__init__(width=size, height=size, x, y, id)

    def __str__(self):
        """ """

        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.height))
