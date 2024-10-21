#!/usr/bin/python3

"""
square.py

This module provides a 'Square' class that iherits the
'Rectangle' class of 'rectangle.py' module.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits the 'Rectangle' class of 'rectangle.py'"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Calls the constructor of the Rectangle class and the
        width and height values are set to 'size'.
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overrides the __str__ method to return a formatted output"""

        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.height))

    @property
    def size(self):
        """Getter for size, which is the same as width """

        return self.width

    @size.setter
    def size(self, value):
        """Setter for size, which updates both width and height"""

        self.width = value
        self.height = value
