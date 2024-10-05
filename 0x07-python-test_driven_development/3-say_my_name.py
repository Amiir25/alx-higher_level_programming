#!/usr/bin/python3
"""
    This program provides a function that prints
    the string "My name is" followed by the name
    passed to the function.
"""

def say_my_name(first_name, last_name=""):
    """
    This function prints "My name is" followed by
    first_name and last_name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
