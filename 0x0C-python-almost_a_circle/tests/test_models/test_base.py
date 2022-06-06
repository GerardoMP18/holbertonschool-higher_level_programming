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
        b7 = Base(-1)
        b8 = Base(-10)
        b9 = Base(-10.5)
        b10 = Base()
        self.assertEqual(b7.id, -1)
        self.assertEqual(b8.id, -10)
        self.assertEqual(b9.id, -10.5)
        self.assertEqual(b10.id, 4)

    def test_base_number_ramdom(self):
        b11 = Base(10.5)
        b12 = Base(1.5)
        b13 = Base(100)
        b14 = Base(-12.5)
        self.assertEqual(b11.id, 10.5)
        self.assertEqual(b12.id, 1.5)
        self.assertEqual(b13.id, 100)
        self.assertEqual(b14.id, -12.5)
