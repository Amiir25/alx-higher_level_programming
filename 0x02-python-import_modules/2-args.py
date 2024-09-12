#!/usr/bin/python3
import sys

if __name__ == "__main__":
    len = len(sys.argv) - 1

    if len == 0:
        print("0 arguments.")

    else:
        if len == 1:
            print("1 argument:")
        else:
            print("{} arguments:".format(len))

        counter = 0
        for i in sys.argv:
            if counter == 0:
                counter += 1
                continue

            print("{}: {}".format(counter, sys.argv[counter]))
            counter += 1
