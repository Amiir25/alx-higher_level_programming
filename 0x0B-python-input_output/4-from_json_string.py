#!/usr/bin/python3

"""
4-from_json_string.py

This module provides a function that returns an object
(Python data structure) represented by a JSON string.
"""

import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string"""

    return json.loads(my_str)
