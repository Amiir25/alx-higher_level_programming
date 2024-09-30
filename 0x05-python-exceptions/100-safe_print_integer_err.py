#!/usr/bin/python3
import sys


def safe_print_integer(value):

    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True

        return False

    except TypeError:
        print("Exception", sys.stderr)
