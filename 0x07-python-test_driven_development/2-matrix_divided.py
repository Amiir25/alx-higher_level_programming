#!/usr/bin/python3
"""
    This module provides a function that divides
    elements of a martix by a given integer and 
    returns a new matrix.
"""

def matrix_divided(matrix, div):
    """
    This function divides elements of a matrix by a
    given number and returns a new matrix consisting
    the result of each division
    """

    if len(matrix) == 0:
        return

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("Each element of the matrix must be a number")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))

        new_matrix.append(new_row)

    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("")
