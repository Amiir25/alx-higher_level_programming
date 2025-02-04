#!/usr/bin/python3
'''
8-json_api.py

Sends a POST request with a letter using 'requests' package.
'''

import requests
import sys


def main():
    '''
    Sends a POST request with a letter 'q' and extracts 'name' and
    'id' values of the response if it is a valid JSON.
    '''

    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) == 2 else ""

    data = {"q": letter}
    response = requests.post(url, data=data)

    try:
        response_json = response.json()
        if not response_json:
            return "No result"

        id = response_json.get("id")
        name = response_json("name")

        print("[{}] {}".format(id, name))

    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
