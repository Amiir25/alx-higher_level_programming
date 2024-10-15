#!/usr/bin/python3

"""
3-to_json_string.py

This module provides a function that returns the
JSON representaion of an object.
"""

import json


def to_json_string(my_obj):
    """Returns a JSON represerntation of an object"""

    return json.dumps(my_obj)
