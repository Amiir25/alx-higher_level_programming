#!/usr/bin/python3

"""
0-read_file.py

This module provides a function that reads a file
and prints it in stdout
"""


def read_file(filename=""):
    """Reads a file and prints it in stdout"""

    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
