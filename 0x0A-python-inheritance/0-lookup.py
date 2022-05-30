#!/usr/bin/python3
'''
function that returns the list of available attributes and methods of an object
'''


def lookup(obj):
    x = dir(obj)
    return x
