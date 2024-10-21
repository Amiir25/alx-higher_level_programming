#!/usr/bin/python3

"""
base.py

This module provides a class 'Base' which used as a base of
all other classes in the project 'Python Almost a Circle'.
"""

import json


class Base:
    """Manages the id attribute"""

    # Private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiates 'id' public instance attribute with the argument
        id value. If 'id' is None, it incerements the '__nb_objects'
        private class attribute and assignes the value to 'id'

        Args:
            id (int): the id value
        """

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the json string representation of a list of dictionaries"""

        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes a json string representation of an argument to a file"""

        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding='utf-8') as f:
            if not list_objs:
                f.write("[]")

            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(list_dict)
                f.write(json_string)
