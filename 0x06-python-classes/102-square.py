#!/usr/bin/python3
"""Compare 2 squares"""


class Square:
    """Creating of instantiation with size
       private instance attibute size
    """
    def __init__(self, size=0):
        self.__size = size
        if(type(self.__size) is not int):
            raise TypeError("size must be an integer")
        if(self.__size < 0):
            raise ValueError("size must be >= 0")

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
