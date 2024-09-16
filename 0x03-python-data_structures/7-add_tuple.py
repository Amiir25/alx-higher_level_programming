#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    a0, a1 = tuple_a[0], tuple_a[1]
    b0, b1 = tuple_b[0], tuple_b[1]

    return (a0 + b0, a1 + b1)
