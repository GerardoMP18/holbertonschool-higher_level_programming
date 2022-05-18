#!/usr/bin/python3
"""Coordinates of a square"""


class Square:
    """Creating of instantiation with size
       private instance attibute size
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        if(type(self.__size) is not int):
            raise TypeError("size must be an integer")
        if(self.__size < 0):
            raise ValueError("size must be >= 0")

        if type(self.__position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif(type(self.__position[0]) and type(self.__position[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif(self.__position[0] < 0 or self.__position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

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
            for i in range(self.__position[1]):
                print()
            for y in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for z in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif(type(value[0]) and type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif(value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
