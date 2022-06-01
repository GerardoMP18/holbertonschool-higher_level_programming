#!/usr/bin/python3
"""
Student to JSON
"""


class Student:
    """
    Class creation to return the representation of the dictionary
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if(type(attrs) is list):
            new_list = {}
            for i in attrs:
                try:
                    new_list[i] = self.__dict__[i]
                except Exception:
                    pass
        else:
            new_list = self.__dict__

        return new_list
