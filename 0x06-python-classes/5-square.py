#!/usr/bin/python3
"""Access and update private attribute"""


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

    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print()
