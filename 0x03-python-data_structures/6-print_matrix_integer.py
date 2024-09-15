#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    x = 0
    for i in matrix:
        y = 0
        for j in range(len(matrix[x])):
            print(f"{i[y]} ", end='')
            y += 1
        x += 1
        print('')
