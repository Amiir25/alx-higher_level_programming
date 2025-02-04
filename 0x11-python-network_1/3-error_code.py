#!/usr/bin/python3
'''
3-error_code.py

Sends a request to a URL and desplays the body of the response with
exception handling
'''

import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)

    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
