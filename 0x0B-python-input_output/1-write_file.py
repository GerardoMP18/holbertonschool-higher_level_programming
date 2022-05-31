#!/usr/bin/python3
"""
Write to a file
"""


def write_file(filename="", text=""):
    """
    Function to write in file
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return myFile.write(text)
