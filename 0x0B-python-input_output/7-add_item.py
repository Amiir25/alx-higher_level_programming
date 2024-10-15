#!/usr/bin/python3

"""
7-add_item.py

This module adds all arguments in a Python list and
save the to a file.
"""

import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if os.path.exists(filename):
    items = load_from_json_file(filename)

else:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, filename)
