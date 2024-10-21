#!/usr/bin/python3

"""
rectangle.py

This module provides a class 'Rectangle' that inherits the 'Base'
class of 'base.py' module.
"""

from models.base import Base


class Rectangle(Base):
    """Inherits the 'Base' class of 'base.py' module"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        calls the super class constructor with 'id' and instantiates
        four private instance attributes
        """

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Overrides the __str__ method to return a formatted output"""

        return ("[Rectangle] ({}) {}/{} - {}/{}".
                format(self.id, self.x, self.y, self.width, self.height))

    # Getter and Setter for width
    @property
    def width(self):
        """getter for the private __width attribute"""

        return self.__width

    @width.setter
    def width(self, width):
        """setter for the private __width attribute"""

        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    # Getter and Setter for height
    @property
    def height(self):
        """getter for the private __height attribute"""

        return self.__height

    @height.setter
    def height(self, height):
        """setter for the private __height attribute"""

        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    # Getter and Setter for x
    @property
    def x(self):
        """getter for the private __x attribute"""

        return self.__x

    @x.setter
    def x(self, x):
        """getter for the private __x attribute"""

        if not isinstance(x, int):
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    # Getter and Setter for y
    @property
    def y(self):
        """getter for the private __y attribute"""

        return self.__y

    @y.setter
    def y(self, y):
        """getter for the private __y attribute"""

        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y

    def area(self):
        """Returns the area of the Rectangle instance"""

        return self.width * self.height

    def display(self):
        """
        Prints 'y' amount of new line, 'x' amount of space and
        the 'Rectangle' instance with the character #
        """

        print("\n" * self.y, end='')

        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Assignes values to attributes using *args or **kwargs"""

        attr = ["id", "width", "height", "x", "y"]

        for index, value in enumerate(args):
            if index < len(attr):
                setattr(self, attr[index], value)

        if not args:
            for key, value in kwargs.items():
                if key in attr:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of Rectangle"""

        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
