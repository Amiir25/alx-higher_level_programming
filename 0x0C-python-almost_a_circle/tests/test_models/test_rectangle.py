#!/usr/bin/python3

"""
test_rectangle.py

A test file for the 'rectangle.py' module
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests the 'Rectangle' class"""

    def test_constructor(self):
        """Tests constructor with and without optional arguments"""

        r1 = Rectangle(3, 4)
        r2 = Rectangle(3, 4, 1, 2, 10)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 2)
        self.assertEqual(r2.id, 10)

    def test_area(self):
        """Tests the area"""

        r = Rectangle(5, 5)
        self.assertEqual(r.area(), 25)

    def test_update_args(self):
        """Tests update method with args"""

        r = Rectangle(3, 4, 1, 2, 10)
        r.update(20, 10, 5, 3, 4)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)

    def test_update_kwargs(self):
        """Tests update method with kwargs"""

        r = Rectangle(3, 4, 1, 2, 10)
        r.update(id=30, width=7, height=6)
        self.assertEqual(r.id, 30)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 6)

    def test_to_dictionary(self):
        """Tests conversion of rectangle to dictionary"""

        r = Rectangle(3, 4, 1, 2, 10)
        r_dict = r.to_dictionary()
        expected = {'id': 10, 'width': 3, 'height': 4, 'x': 1, 'y': 2}
        self.assertEqual(r_dict, expected)

    def test_str(self):
        """Tests __str__ method output"""

        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")


if __name__ == "__main__":
    unittest.main()
