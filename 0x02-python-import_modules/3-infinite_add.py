#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    sum = 0
    c = 0

    if len(argv) == 1:
        print(0)

    else:
        for i in argv:
            if c == 0:
                c += 1
                continue
            sum += int(argv[c])
            c += 1

        print(sum)
