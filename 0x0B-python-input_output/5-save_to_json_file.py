#!/usr/bin/python3

"""
5-save_to_json_file.py

This file defines a function that writes an object to a
text file, using a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON"""

    data = json.dumps(my_obj)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(data)
