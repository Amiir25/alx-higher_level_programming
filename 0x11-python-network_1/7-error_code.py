#!/usr/bin/python3
'''
7-error_code.py

Sends a request to a URL and desplays the body of the response with
exception handling using 'requests' package
'''

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code:", response.status_code)

    else:
        print(response.text)
