#!/usr/bin/python3
"""  script that takes in a URL, sends a request to the URL and displays
    the body of the response decoded in utf-8 """


import sys
from urllib import request, parse, error


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print("{}".format(body))
    except error.HTTPError as error:
        print("Error code: {}".format(error.code))
