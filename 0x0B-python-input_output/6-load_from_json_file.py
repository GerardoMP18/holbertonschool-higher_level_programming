#!/usr/bin/python3
"""
Create object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Function to create an object from Json File
    """
    with open(filename, mode='r', encoding='utf-8') as myFile:
        return json.loads(myFile.read())
