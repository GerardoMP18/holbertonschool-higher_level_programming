#!/usr/bin/python3
"""
 Search and update
"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file
    """
    with open(filename, mode="r", encoding="utf-8") as myFile:
        list_text = myFile.readlines()

    with open(filename, mode="w", encoding="utf-8") as myFile2:
        for read in list_text:
            myFile2.write(read)
            if search_string in read:
                myFile2.write(new_string)
