#!/usr/bin/python3
"""
Integers addition

Write a function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    Function for sum 2 number intergers
    """
    suma = 0
    if (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    elif (type(b) is not int and type(b) is not float):
        raise TypeError("b must be an integer")

    if (type(a) is float):
        a = int(a)
    elif (type(b) is float):
        b = int(b)

    suma = a + b
    return suma
