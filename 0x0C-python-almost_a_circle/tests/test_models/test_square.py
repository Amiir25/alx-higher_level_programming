#!/usr/bin/python3

"""
test_square.py

Test file for 'square.py' module
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests the 'Square' class"""

    def test_constructor(self):
        """Tests constructor with size, x, y, id."""

        s1 = Square(5)
        s2 = Square(10, 2, 3, 99)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.id, 99)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)

    def test_area(self):
        """Tests the area"""

        s = Square(6)
        self.assertEqual(s.area(), 36)

    def test_update_args(self):
        """Tests update method with args."""

        s = Square(3, 2, 1, 20)
        s.update(30, 5, 4, 6)
        self.assertEqual(s.id, 30)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 6)

    def test_update_kwargs(self):
        """Tests update method with kwargs."""

        s = Square(3, 2, 1, 20)
        s.update(id=40, size=8, x=5, y=7)
        self.assertEqual(s.id, 40)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 7)

    def test_to_dictionary(self):
        """Tests conversion of Square to dictionary"""

        s = Square(5, 3, 2, 10)
        s_dict = s.to_dictionary()
        expected = {'id': 10, 'size': 5, 'x': 3, 'y': 2}
        self.assertEqual(s_dict, expected)

    def test_str(self):
        """Test __str__ method output."""

        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")


if __name__ == "__main__":
    unittest.main()
