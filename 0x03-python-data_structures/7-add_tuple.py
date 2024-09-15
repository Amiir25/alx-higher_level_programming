#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    w = tuple_a[0]
    x = 0 if len(tuple_a) < 2 else tuple_a[1]
    if len(tuple_a) < 1:
        w, x = 0, 0

    y, z = 0, 0
    if len(tuple_b) < 1:
        y, z = 0, 0
    else:
        y = tuple_b[0]
        z = 0 if len(tuple_b) < 2 else tuple_b[1]

    new_tuple = (w + y, x + z)
    return new_tuple
