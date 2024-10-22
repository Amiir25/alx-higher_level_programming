#!/usr/bin/python3

"""
test_base.py

A test file for the 'base.py' module
"""

import unittest
from models.base import Base


class TestBase(unittest.Testcase):
    """Test the 'Base' class"""

    def test_auto_increment_id(self):
        """Tests automatic id assignment"""

        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_manual_id(self):
        """Tests manual id assignment"""

        b3 = Base(100)
        self.assertEqual(b3.id, 100)

    def test_to_json_string(self):
        """Tests conversion of list of dictionaries to JSON string"""

        dict_list = [{'id': 1}, {'id': 2}]
        json_string = Base.to_json_string(dict_list)
        self.assertEqual(json_string, '[{"id": 1}, {"id": 2}]')

    def test_from_json_string(self):
        """Tests conversion of JSON string to list of dictionaries"""

        json_string = '[{"id": 1}, {"id": 2}]'
        dict_list = Base.from_json_string(json_string)
        self.asserEqual(dict_list, [{'id': 1}. {'id': 2}])

    def test_create(self):
        """Tests create method creates instance with attributes."""

        from models.rectangle import Rectangle

        dict = {'id': 1, 'width': 3, 'height': 2, 'x': 0, 'y': 0}
        rect = Rectangle.create(**dict)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 2)

    def test_save_to_file(self):
        """Tests saving list of instances to file."""

        from models.rectangle import Rectangle

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open('Rectangle.json', 'r', encoding='utf-8') as file:
            content = file.read()
            self.assertIn('"width": 10', content)
            self.assertIn('"height": 7', content)

    def test_load_from_file(self):
        """Test loading list of instances from file."""

        from models.rectangle import Rectangle

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        loaded_rectangles = Rectangle.load_from_file()

        self.assertEqual(len(loaded_rectangles), 2)
        self.assertEqual(loaded_rectangles[0].width, 10)
        self.assertEqual(loaded_rectangles[1].height, 4)


if __name__ == "__main__":
    unittest.main()
