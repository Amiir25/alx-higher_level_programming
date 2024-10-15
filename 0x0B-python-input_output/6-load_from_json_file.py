#!/usr/bin/python3

"""
This file defines a function that creates an object
from JSON file
"""

import json


def load_from_json_file(filename):
    """Creates an object from JSON file"""

    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
