#!/usr/bin/python3
'''
2-post_email.py

Sends a POST request to the passed URL with the email as a
parameter, and displays the body of the response.
'''

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({"email": email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method="POST")

    with urllib.request.urlopen(req) as response:
        your_email = response.read().decode('utf-8')
        print(your_email)
