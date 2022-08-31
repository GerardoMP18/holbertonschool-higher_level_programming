#!/usr/bin/python3
""" script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter """


import sys
import requests


if __name__ == "__main__":
    size = len(sys.argv)
    url = 'http://0.0.0.0:5000/search_user'
    if size == 1:
        q = ""
    else:
        q = sys.argv[1]
    obj = {'q': q}
    res = requests.post(url, data=obj)
    try:
        mydict = res.json()
        if mydict:
            print("[{}] {}".format(mydict['id'], mydict['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
