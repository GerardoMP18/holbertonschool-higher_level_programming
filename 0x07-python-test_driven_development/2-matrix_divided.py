#!/usr/bin/python3
"""
Divide a matrix

Write a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Function that allows to perform matrix division
    """
    new_matrix = []
    if (type(matrix) is not list):
        raise TypeError("matrix must be a matrix (list of lists) of integers" +
                        "/floats")
    elif (type(div) is not int and type(div) is not float):
        raise TypeError("div must be a number")
    elif (div == 0):
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        if (len(matrix[i]) is not len(matrix[0])):
            raise TypeError("Each row of the matrix must have the same size")
        for j in matrix[i]:
            if (type(j) is not int and type(j) is not float):
                raise TypeError("matrix must be a matrix (list of lists)" +
                                " of integers/floats")

    for x in matrix:
        new_matrix.append(list(map(lambda x: round(x / div, 2), x)))

    return new_matrix
