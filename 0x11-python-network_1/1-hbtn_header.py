#!/usr/bin/python3
'''
1-hbtn_header.py

Sends a request to a URL and prints the  X-Request-ID value of the
response's header
'''

import urllib.request
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    request = urllib.request.Request(url)

    with urllib.request.urlopen(request) as response:
        header = response.info()
        print(header.get("X-Request-ID"))
