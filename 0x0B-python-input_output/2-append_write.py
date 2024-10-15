#!/usr/bin/python3

"""
2-append_write.py

This module provides a function that appends a string
to the end of a text file and returns the number of
characters appended.
"""


def append_write(filename="", text=""):
    """
    Appends to the end of a file and returns the number of
    characters appended
    """

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
