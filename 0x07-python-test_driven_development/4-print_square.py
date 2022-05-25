#!/usr/bin/python3
"""
Print square

Write a function that prints a square with the character #
"""


def print_square(size):
    """
    Function that will print the amount of "#" characters according
    to the given value
    """
    if(type(size) is not int):
        raise TypeError("size must be an integer")
    elif(size < 0):
        raise ValueError("size must be >= 0")

    for x in range(size):
        for z in range(size):
            print("#", end="")
        print()
