#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    len = len(argv)

    if len == 1:
        print("0 arguments.")

    else:
        if len == 2:
            print("1 argument:")
        else:
            print("{} arguments:".format(len - 1))

        c = 0
        for i in argv:
            if c == 0:
                c += 1
                continue

            print("{}: {}".format(c, argv[c]))
            c += 1
