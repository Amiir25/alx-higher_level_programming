#!/usr/bin/python3

letters = ''
for i in range(ord('a'), ord('z') + 1):
    letters += chr(i)

print("{}".format(letters), end='')
