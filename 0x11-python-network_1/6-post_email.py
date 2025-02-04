#!/usr/bin/python3
'''
6-post_email.py

Sends a POST request with email as a parameter, and displays the body
of the response using 'requests' package
'''

import requests
import sys


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: ./6-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}
    responses = requests.post(url, data=data)

    print(response.text)
