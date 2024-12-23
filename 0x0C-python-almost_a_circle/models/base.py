#!/usr/bin/python3

"""
base.py

This module provides a class 'Base' which used as a base of
all other classes in the project 'Python Almost a Circle'.
"""

import json
import os


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
        """
        Converts a list of instances into a list of dictionaries and writes
        a json string representation of the list of dictionaries to a file
        """

        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding='utf-8') as f:
            if not list_objs:
                f.write("[]")

            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(list_dict)
                f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the json string representation"""

        if not json_string:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all atributes already set"""

        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)

        elif cls.__name__ == "Square":
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""

        filename = "{}.json".format(cls.__name__)

        if not os.path.exists(filename):
            return []

        with open(filename, 'r', encoding='utf-8') as file:
            json_string = file.read()
            list_dict = cls.from_json_string(json_string)

        return [cls.create(**d) for d in list_dict]
