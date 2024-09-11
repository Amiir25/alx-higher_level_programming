#!/usr/bin/python3

def islower(c):
    case = ord(c)

    if (case >= ord('a') and case <= ord('z')):
        return True
    else:
        return False
