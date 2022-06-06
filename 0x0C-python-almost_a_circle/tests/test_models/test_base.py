#!/usr/bin/python3
import unittest
from models.base import Base
"""
Unittest for class Base
"""


class TestClassBase(unittest.TestCase):
    """Testing with unittest"""
    def test_base(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(30)
        self.assertEqual(b3.id, 30)
        b4 = Base(25)
        self.assertEqual(b4.id, 25)
        b5 = Base()
        self.assertEqual(b5.id, 3)

    def test_base_number_negative(self):
        b1 = Base(-1)
        b2 = Base(-10)
        b3 = Base(-10.5)
        b4 = Base()
        self.assertEqual(b1.id, -1)
        self.assertEqual(b2.id, -10)
        self.assertEqual(b3.id, -10.5)
        self.assertEqual(b4.id, 4)

