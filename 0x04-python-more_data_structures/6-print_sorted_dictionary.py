#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    orden = sorted(a_dictionary)
    for x in orden:
        print("{}: {}".format(x, a_dictionary[x]))
