#!/usr/bin/python3

for i in range(0, 9):
    for j in range(1, 10):
        if (i == j or int(f"{i}{j}") > int(f"{j}{i}")):
            continue

        if (i < 8):
            print("{}{}, ".format(i, j), end='')

        else:
            print("{}{}".format(i, j))
