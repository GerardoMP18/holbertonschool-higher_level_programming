#!/usr/bin/python3
"""
Append to a file
"""


def append_write(filename="", text=""):
    """
    Function to append and create in new file"
    """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return myFile.write(text)
