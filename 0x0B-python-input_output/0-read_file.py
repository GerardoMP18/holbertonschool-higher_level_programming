#!/usr/bin/python3
"""
Function read file
"""


def read_file(filename=""):
    """
    Function to read the file utf-8
    """
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")
