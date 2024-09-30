#!/usr/bin/python3
import sys


def safe_print_integer_err(value):

    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True

    except TypeError as e:
        print("Exeption: {}".format(e), file=sys.stderr)
        return False
