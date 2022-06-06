#!/usr/bin/python3
"""
- Base class
- Dictionary to JSON string
- JSON string to file
- JSON string to dictionary
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        JSON string representation of list_objs in a file
        """
        new_list = []
        if list_objs:
            for i in list_objs:
                dictionary = i.to_dictionary()
                new_list.append(dictionary)
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8")as myFile:
            myFile.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Static method to return a json list to a string representation
        """
        if json_string is None or json_string == []:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns the instance with all attributes set
        """
        rectangle = cls.__name__
        square = cls.__name__
        if dictionary:
            if(rectangle == 'Rectangle'):
                dummy = cls(1, 2, 3, 4)
            if(square == 'Square'):
                dummy = cls(5)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as myFile:
                readFile = myFile.read()
                list_dictionary = cls.from_json_string(readFile)
                new = []
                for items in list_dictionary:
                    new.append(cls.create(**items))
                return new
        except Exception:
            return []
