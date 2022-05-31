#!/usr/bin/python3
"""
Save Object to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function to append in new file of in json
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(json.dumps(my_obj))
