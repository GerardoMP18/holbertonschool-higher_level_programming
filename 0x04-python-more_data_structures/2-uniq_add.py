#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set(my_list)
    for i in unique:
        unique.add(i)
    return sum(unique)
