#!/usr/bin/python3
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
"""
Unittest for class Base
"""


class TestClassBase(unittest.TestCase):
    """Testing with unittest"""
    def test_base(self):
        """Test for class Base with number ramdom"""
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
        """Test with number negative in class base"""
        b7 = Base(-1)
        b8 = Base(-10)
        b9 = Base(-10.5)
        b10 = Base()
        self.assertEqual(b7.id, -1)
        self.assertEqual(b8.id, -10)
        self.assertEqual(b9.id, -10.5)

    def test_base_number_ramdom(self):
        """Test with number ramdom"""
        b11 = Base(10.5)
        b12 = Base(1.5)
        b13 = Base(100)
        b14 = Base(-12.5)
        self.assertEqual(b11.id, 10.5)
        self.assertEqual(b12.id, 1.5)
        self.assertEqual(b13.id, 100)
        self.assertEqual(b14.id, -12.5)

    def test_base_to_json_string(self):
        """Test with method to_json_string"""
        dictionary = {'x': 9, 'width': -1, 'id': 1.5, 'height': 10, 'y': 11}
        json_dictionary = Base.to_json_string([dictionary])
        result = '[{"x": 9, "width": -1, "id": 1.5, "height": 10, "y": 11}]'
        self.assertEqual(json_dictionary, result)
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(json_dictionary), str)

    def test_base_to_json_string_None(self):
        """Test with method to_json_string with paramater None"""
        dictionary = None
        json_dictionary = Base.to_json_string(dictionary)
        self.assertEqual(json_dictionary, "[]")

    def test_base_to_json_string_empty(self):
        """Test with method to_json_string with paramaeters empty"""
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, "[]")

    def test_base_save_to_file_Rectangle(self):
        """Test with method save_to_file with class Rectangle"""
        r1 = Rectangle(11, 7, 2, 8)
        r2 = Rectangle(2, 9)
        Rectangle.save_to_file([r1, r2])
        result = ('[{"y": 8, "x": 2, "id": 1, "width": 11, "height": 7},' +
                  ' {"y": 0, "x": 0, "id": 2, "width": 2, "height": 9}]')
        with open("Rectangle.json", "r") as myFile:
            self.assertEqual(len(myFile.read()), len(result))

        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_base_save_to_file_square(self):
        """Test with method save_to_file with class Square"""
        r3 = Square(11, 3, 2)
        Square.save_to_file([r3])
        result = ('[{"id": 1, "x": 3, "size": 11, "y": 2}]')
        with open("Square.json", "r") as myFile:
            self.assertEqual(len(myFile.read()), len(result))

        self.assertTrue(os.path.exists("Square.json"))

    def test_base_save_to_file_None(self):
        """Test with method save_to_file with class Square and
        Rectangle with parameters None"""
        Square.save_to_file(None)
        Rectangle.save_to_file(None)
        result = "[]"
        with open("Square.json", "r") as myFile:
            self.assertEqual(myFile.read(), result)

        with open("Rectangle.json", "r") as myFile2:
            self.assertEqual(myFile2.read(), result)

    def test_base_save_to_file_list_empty(self):
        """Test with method save_to_file with class Square and
        Rectangle with parameters Empty"""
        Square.save_to_file([])
        Rectangle.save_to_file([])
        result = "[]"
        with open("Square.json", "r") as myFile:
            self.assertEqual(myFile.read(), result)

        with open("Rectangle.json", "r") as myFile2:
            self.assertEqual(myFile2.read(), result)

    def test_from_json_string(self):
        """Test of from_json_string with class Rectangle"""
        list_input = [
            {'id': 70, 'width': -10, 'height': 10},
            {'id': 6, 'width': 6, 'height': 5}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        result = [{'id': 70, 'width': -10, 'height': 10},
                  {'id': 6, 'width': 6, 'height': 5}]
        self.assertEqual(list_output, result)

    def test_from_json_string_None(self):
        """Test of from_json_string with class Rectangle with parameter None"""
        list_output = Rectangle.from_json_string(None)
        result = []
        self.assertEqual(list_output, [])

    def test_from_json_string_empty(self):
        """Test of from_json_string with class Rectangle with parameter
        Empty"""
        list_output = Rectangle.from_json_string([])
        result = []
        self.assertEqual(list_output, [])

    def test_create(self):
        """Test of method create with class Rectangle and Square"""
        r1 = Rectangle(3, 5, 1, 2, 10)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Rectangle] (10) 1/2 - 3/5")
        self.assertEqual(str(r2), "[Rectangle] (10) 1/2 - 3/5")
        self.assertIsNot(r1, r2)

        r3 = Square(3, 1, 3, 20)
        r3_dictionary = r3.to_dictionary()
        r4 = Square.create(**r3_dictionary)
        self.assertEqual(str(r3), "[Square] (20) 1/3 - 3")
        self.assertEqual(str(r4), "[Square] (20) 1/3 - 3")
        self.assertIsNot(r3, r4)

    def test_load_from_file(self):
        """Test of method load_from_file with class Rectangle and
        Square"""
        r10 = Rectangle(10, 7, 2, 8, 25)
        r20 = Rectangle(20, 5, 6, 8, 100)
        list_rectangles_input = [r10, r20]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r20), str(list_rectangles_output[1]))

        r30 = Square(10, 20, 30, 40)
        r40 = Square(15, 5, 25, 150)
        list_square_input = [r30, r40]
        Square.save_to_file(list_square_input)
        list_square_output = Square.load_from_file()
        self.assertEqual(str(r30), str(list_square_output[0]))
