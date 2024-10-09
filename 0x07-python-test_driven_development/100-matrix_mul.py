#!/usr/bin/python3

"""
100-matrix_mul.py

This module provides a function that multiplies two
matrices
"""


def matrix_mul(m_a, m_b):
    """A function that multiplies two matrices"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")

        if m_a == [] or row == []:
            raise ValueError("m_a can't be empty")

        for element in row:
            if type(element) not in [int, float]:
                raise ValueError("m_a should contain only integers or floats")

        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same type")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")

        if m_b == [] or row == []:
            raise ValueError("m_b can't be empty")

        for element in row:
            if type(element) not in [int, float]:
                raise ValueError("m_b should contain only integers or floats")

        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same type")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    """Diving in"""

    new_matrix = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                new_matrix[i][j] += m_a[i][k] * m_b[k][j]

    return new_matrix
