#!/usr/bin/pyhton3

"""
6-max_integer_test.py

Unittest for max_integer([...])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test class for mac_integer function."""

    def test_normal_list(self):
        """Test with a list of positive integers"""

        self.assertAlmostEqual(max_integer([1, 2, 3 ,4]), 4)

    def test_empty_list(self):
        """Test with empty list."""

        self.assertAlmostEqual(max_integer([]), None)

    def test_single_element(self):
        """Test with single element."""

        self.assertAlmostEqual(max_integer([4]), 4)

    def test_negative_numbers(self):
        """Test with a list of negative numbers"""

        self.assertAlmostEqual(max_integer([-7, -6, -5 ,-4]), -4)

    def test_mixed_numbers(self):
        """Test with a list that contains both positive and negative numbers"""

        self.assertAlmostEqual(max_integer([1, -2, -3 ,4]), 4)

    def test_same_numbers(self):
        """Test with a list where all elements are the same."""

        self.assertAlmostEqual(max_integer([4, 4, 4 ,4]), 4)

    def test_float_numbers(self):
        """Test with a list of float numbers"""

        self.assertAlmostEqual(max_integer([1.1, 2.2, 3.3 ,4.4]), 4.4)

    def test_with_zero(self):
        """Test with a list that contains zero"""

        self.assertAlmostEqual(max_integer([1, 2, 0 ,4]), 4)

    def test_unordered_list(self):
        """Test with unoredered list"""

        self.assertAlmostEqual(max_integer([44, 3, -98 ,29]), 44)

    def test_normal_list(self):
        """Test with a list of positive integers"""

        self.assertAlmostEqual(max_integer([1, 2, 3 ,4]), 4)

    def test_max_at_beginning(self):
        """Test with a list where tha max is at the beginning"""

        self.assertAlmostEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test with a list where tha max is at the beginning"""

        self.assertAlmostEqual(max_integer([2, 3, 4, -5, -6]), 4)
