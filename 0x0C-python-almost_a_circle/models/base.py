#!/usr/bin/python3
"""
- Base class
- Dictionary to JSON string
- JSON string to file
"""
import json


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

    """
    Return the JSON string representation of list_dictionaries
    """
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return (json.dumps(list_dictionaries))

    """
    JSON string representation of list_objs in a file
    """
    @classmethod
    def save_to_file(cls, list_objs):
        new_list = []
        if list_objs:
            for i in list_objs:
                dictionary = i.to_dictionary()
                new_list.append(dictionary)
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8")as myFile:
            myFile.write(cls.to_json_string(new_list))
