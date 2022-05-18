#!/usr/bin/python3
"""My File ByteCode."""


class MagicClass:
    """My first class ByteCode"""
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._radius = radius

    def area(self):
        return self._radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self._radius
