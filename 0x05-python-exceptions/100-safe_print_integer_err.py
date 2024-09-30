#!/usr/bin/python3

def safe_print_integer_err(value):

    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True

    except TypeError as e:
        import sys

        print("Exeption: {}".format(e), file=sys.stderr)
        return False
