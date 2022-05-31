#!/usr/bin/python3
"""
Module import to be able to inherit the BaseGeometry class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Instantiation with size: def __init__(self, size)
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    """
    Return description of square
    """
    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
