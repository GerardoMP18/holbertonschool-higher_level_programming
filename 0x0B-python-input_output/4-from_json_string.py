#!/usr/bin/python3
"""
From JSON string to Object
"""
import json


def from_json_string(my_str):
    """
    Function to return in objetc in data structure
    represented by JSON strin
    """
    return json.loads(my_str)
