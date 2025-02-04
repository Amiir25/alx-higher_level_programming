#!/usr/bin/python3
'''
5-hbtn_header.py

Sends a request to a URL and prints the  X-Request-ID value of the
response's header using the 'requests' package
'''

import requests
import sys


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    response = requests.get(url)
    print(response.headers.get("X-Request-ID"))
