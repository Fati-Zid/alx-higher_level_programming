#!/usr/bin/python3
'''Module for Rectangle unit tests.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    '''Class to test the Rectangle class.'''

    def test_class_exists(self):
        '''Check if Rectangle exists.'''

        self.assertTrue(hasattr(Rectangle, '__init__'))
        self.assertTrue(hasattr(Rectangle, 'width'))
        self.assertTrue(hasattr(Rectangle, 'height'))
        self.assertTrue(hasattr(Rectangle, 'x'))
        self.assertTrue(hasattr(Rectangle, 'y'))
        self.assertTrue(issubclass(Rectangle, Base))

    def test_create_rectangle_instance_with_width_height(self):
        '''Create a rectangle instance with width and height.'''

        rectangle_instance = Rectangle(10, 20)
        self.assertEqual(rectangle_instance.id, 1)
        self.assertEqual(rectangle_instance.width, 10)
        self.assertEqual(rectangle_instance.height, 20)
        self.assertEqual(rectangle_instance.x, 0)
        self.assertEqual(rectangle_instance.y, 0)

    def test_create_rectangle_instance_with_width_height_x(self):
        '''Create a rectangle instance with width, height and x.'''

        rectangle_instance = Rectangle(10, 20, 5)
        self.assertEqual(rectangle_instance.id, 2)
        self.assertEqual(rectangle_instance.width, 10)
        self.assertEqual(rectangle_instance.height, 20)
        self.assertEqual(rectangle_instance.x, 5)
        self.assertEqual(rectangle_instance.y, 0)

    def test_create_rectangle_instance_with_width_height_x_y(self):
        '''Create a rectangle instance with width, height, x and y.'''

        rectangle_instance = Rectangle(10, 20, 5, 8)
        self.assertEqual(rectangle_instance.id, 3)
        self.assertEqual(rectangle_instance.width, 10)
        self.assertEqual(rectangle_instance.height, 20)
        self.assertEqual(rectangle_instance.x, 5)
        self.assertEqual(rectangle_instance.y, 8)

    def test_create_rectangle_instance_with_width_height_x_y_id(self):
        '''Create a rectangle instance with width, height, x, y and id.'''

        rectangle_instance = Rectangle(10, 20, 5, 8, 100)
        self.assertEqual(rectangle_instance.id, 100)
        self.assertEqual(rectangle_instance.width, 10)
        self.assertEqual(rectangle_instance.height, 20)
        self.assertEqual(rectangle_instance.x, 5)
        self.assertEqual(rectangle_instance.y, 8)

    def test_getter_and_setter_for_width(self):
        '''Test getter and setter for width attribute of the rectangle class.'''

        rectangle_instance = Rectangle(10, 20)
        self.assertEqual(rectangle_instance.width, 10)
        rectangle_instance.width = 15
        self.assertEqual(rectangle_instance.width, 15)

    def test_getter_and_setter_for_height(self):
        '''Test getter and setter for height attribute of the rectangle class.'''

        rectangle_instance = Rectangle(10, 20)
        self.assertEqual(rectangle_instance.height, 20)
        rectangle_instance.height = 25
        self.assertEqual(rectangle_instance.height, 25)

    def test_getter_and_setter_for_x(self):
        '''Test getter and setter for x attribute of the rectangle class.'''

        rectangle_instance = Rectangle(10, 20, 5)
        self.assertEqual(rectangle_instance.x, 5)
        rectangle_instance.x = 3
        self.assertEqual(rectangle_instance.x, 3)

    def test_getter_and_setter_for_y(self):
        '''Test getter and setter for y attribute of the rectangle class.'''

        rectangle_instance = Rectangle(10, 20, 5, 8)
        self.assertEqual(rectangle_instance.y, 8)
        rectangle_instance.y = 6
        self.assertEqual(rectangle_instance.y, 6)

if __name__ == '__main__':
    unittest.main()
