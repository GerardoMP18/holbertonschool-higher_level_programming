#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then save
"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    filejson = "add_item.json"
    my_list = load_from_json_file(filejson)
except Exception as e:
    my_list = []

save_to_json_file(my_list + argv[1:], filejson)
