#!/usr/bin/python3
"""
Write a class MyInt that inherits from int
"""


class MyInt(int):
    """
    Write operator inverted
    """
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        return self.number != other

    def __ne__(self, other):
        return self.number == other
