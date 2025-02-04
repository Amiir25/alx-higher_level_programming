#!/usr/bin/python3
'''
4-hbtn_status.py

Fetches a URL using the 'requests' package
'''

import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io"
    response = requests.get(url)
    content = response.text.strip()

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content.splitlines()[0])
