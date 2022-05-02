#!/usr/bin/env python3
def no_c(my_string):
    change = ""
    for x in my_string:
        if x not in "cC":
            change = change + x
    return change
