#!/usr/bin/python3

"""
1-write_file.py

This module provides a function that writes a string
to a text file and returns the number of characters
written
"""


def write_file(filename="", text=""):
    """Writes to a file and returns the number of characters written"""

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
