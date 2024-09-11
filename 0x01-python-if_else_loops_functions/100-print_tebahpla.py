#!/usr/bin/python3

counter = 1
for i in reversed(range(ord('a'), ord('z') + 1)):
    if (counter % 2 == 0):
        i = i - 32

    counter += 1
    print(chr(i), end='')
