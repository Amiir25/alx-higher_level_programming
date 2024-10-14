#!/usr/bin/python3

"""
1-my_list.py

This module provides a class that inherits from
the built-in list object.
"""


class MyList(list):
    """Inherits the built-in list object"""

    def print_sorted(self):
        """Prints a sorted list"""

        print(sorted(self))
