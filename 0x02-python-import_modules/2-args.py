#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argv = argv[1:]
    len = len(argv)

    if len == 0:
        print("{} arguments.".format(len))
    elif len == 1:
        print("{} argument:".format(len))
    else:
        print("{} arguments:".format(len))

    for i, arg in enumerate(argv, 1):
        print("{}: {}".format(i, arg))
