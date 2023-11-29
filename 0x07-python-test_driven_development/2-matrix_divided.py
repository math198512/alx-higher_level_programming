#!/usr/bin/python3
"""
This function, matrix_divided,
divides all elements of a matrix by a given number.
"""


def matrix_divided(matrix, div):

    """Returns a new matrix with elements divided by div,
    rounded to 2 decimal places
    """
    errMsg = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix and not isinstance(matrix, list):
        raise TypeError(errMsg)
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(errMsg)
        for item in lists:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError(errMsg)
    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in lists] for lists in matrix]
