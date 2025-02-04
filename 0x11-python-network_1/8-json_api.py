#!/usr/bin/python3
'''
8-json_api.py

Sends a request to a URL and desplays the body of the response with
exception handling using 'requests' package
'''

import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) == 2 else ""

    response = requests.post(url, q)

    try:
        response_json = response.json()
        if not response_json:
            return "No result"

        id = response_json.get("id")
        name = response_json("name")

        print("[{}] {}".format(id, name))

    except ValueError:
        print("Not a valid JSON")
