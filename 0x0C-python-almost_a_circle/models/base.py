#!/usr/bin/python3
"""
Base class
"""


class Base:
    """
    Creation of constructor
    validation of id is not None and incremet in attribute __nb_objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
