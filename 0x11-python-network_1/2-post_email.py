#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status """

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
