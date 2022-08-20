#!/usr/bin/python3
""" Time for an interview! """


import sys
import requests


if __name__ == "__main__":
    nameRepository = sys.argv[1]
    nameOwner = sys.argv[2]
    urlApi = 'https://api.github.com/repos/{}/{}/commits'.format(
            nameOwner, nameRepository)
    res = requests.get(urlApi)
    resJson = res.json()
    for result in resJson[0:10]:
        print("{}: {}".format(result.get('sha'),
                              result.get('commit').get('author').get('name')))
