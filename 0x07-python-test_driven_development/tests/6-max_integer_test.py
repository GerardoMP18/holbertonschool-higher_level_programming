#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Testing with unittest"""
    def test_maximum_integer(self):
        """Test to print the maximum number"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, 10, -1]), 10)
        self.assertEqual(max_integer([1000]), 1000)
        self.assertEqual(max_integer([-1, -9, -2]), -1)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_string(self):
        """Tests to print the error message when taking the
        maximum of a string with number"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'Error', 3])

    def test_empty(self):
        """Tests with empty parameter"""
        self.assertIsNone(max_integer())

    def test_empty_list(self):
        """Tests with list empty parameter"""
        self.assertIsNone(max_integer([]))

    def test_maximun_float(self):
        """Test to print the maximum number float"""
        self.assertEqual(max_integer([2.5, 3.3, 10.5, 100.5]), 100.5)
        self.assertEqual(max_integer([2.5, 5, 10.5, 11.1]), 11.1)
        self.assertEqual(max_integer([2.5, -1, -9, 9.6, 5.3]), 9.6)
        self.assertEqual(max_integer([-1, 10, 0, 15.9, 16]), 16)

    if __name__ == '__main__':
        unittest.main()
