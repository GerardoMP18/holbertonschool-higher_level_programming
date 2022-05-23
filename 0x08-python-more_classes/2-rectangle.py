#!/usr/bin/python3
"""Area and Perimeter"""


class Rectangle:
    """Creating of instantiation with width
        private instance attribute height
    """
    def __init__(self, width=0, height=0):
        """Initialization of rectagule"""
        self.__width = width
        self.__height = height
        if (type(self.__width) is not int):
            raise TypeError("width must be an integer")
        elif(self.__width < 0):
            raise ValueError("width must be >= 0")
        elif (type(self.__height) is not int):
            raise TypeError("height must be an integer")
        elif (self.__height < 0):
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        elif(value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return 2 * (self.__width + self.__height)
