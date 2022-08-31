#!/usr/bin/python3
""" script that takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id """


import sys
import requests


if __name__ == "__main__":
    urlApi = 'https://api.github.com/user'
    user = sys.argv[1]
    password = sys.argv[2]
    res = requests.get(urlApi, auth=(user, password)).json()
    if res.get('id'):
        print("{}".format(res.get('id')))
    else:
        print("None")
