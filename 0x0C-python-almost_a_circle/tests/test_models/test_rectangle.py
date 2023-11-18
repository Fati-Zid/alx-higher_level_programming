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

    def test_area_of_rectangle_10_12(self):
        '''Calculate area of rectangle with width=10 and height=12.'''

        rectangle_instance = Rectangle(10, 12)
        self.assertEqual(rectangle_instance.area(), 120)

    def test_area_of_rectangle_12_10(self):
        '''Calculate area of rectangle with width=12 and height=10.'''

        rectangle_instance = Rectangle(12, 10)
        self.assertEqual(rectangle_instance.area(), 120)

    def test_area_of_rectangle_10_10(self):
        '''Calculate area of rectangle with width=10 and height=10.'''

        rectangle_instance = Rectangle(10, 10)
        self.assertEqual(rectangle_instance.area(), 100)

    def test_area_of_rectangle_10_12_with_x_and_y(self):
        '''Calculate area of rectangle with width=10, height=12, x=4 and y=7.'''

        rectangle_instance = Rectangle(10, 12, 1, 3)
        self.assertEqual(rectangle_instance.area(), 120)

    def test_display_for_rectangle_10_12(self):
        '''Display a rectangle with width=10 and height=12.'''

        rectangle_instance = Rectangle(10, 12)
        captured_output = StringIO()
        sys.stdout = captured_output
        rectangle_instance.display()
        sys.stdout = sys.__stdout__
        expected_output = "##########\n" * 12
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display_for_rectangle_1_12(self):
        '''Display a rectangle with width=1 and height=12.'''

        rectangle_instance = Rectangle(1, 12)
        captured_output = StringIO()
        sys.stdout = captured_output
        rectangle_instance.display()
        sys.stdout = sys.__stdout__
        expected_output = "#\n" * 12
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display_for_rectangle_10_1(self):
        '''Display a rectangle with width=10 and height=1.'''

        rectangle_instance = Rectangle(10, 1)
        captured_output = StringIO()
        sys.stdout = captured_output
        rectangle_instance.display()
        sys.stdout = sys.__stdout__
        expected_output = "##########\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display_for_rectangle_3_3(self):
        '''Display a rectangle with width=3 and height=3.'''

        rectangle_instance = Rectangle(3, 3)
        captured_output = StringIO()
        sys.stdout = captured_output
        rectangle_instance.display()
        sys.stdout = sys.__stdout__
        expected_output = "###\n###\n###\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display_for_rectangle_1_1(self):
        '''Display a rectangle with width=1 and height=1.'''

        rectangle_instance = Rectangle(1, 1)
        captured_output = StringIO()
        sys.stdout = captured_output
        rectangle_instance.display()
        sys.stdout = sys.__stdout__
        expected_output = "#\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str_of_rectangle_10_12(self):
        '''Return the string representation of a rectangle with width=10 and height=12.'''

        rectangle_instance = Rectangle(10, 12)
        expected_output = "[Rectangle] (1) 0/0 - 10/12"
        self.assertEqual(str(rectangle_instance), expected_output)

    def test_str_of_rectangle_12_10(self):
        '''Return the string representation of a rectangle with width=12 and height=10.'''

        rectangle_instance = Rectangle(12, 10)
        expected_output = "[Rectangle] (2) 0/0 - 12/10"
        self.assertEqual(str(rectangle_instance), expected_output)

    def test_str_of_rectangle_12_10_with_x(self):
        '''Return the string representation of a rectangle with width=12 and height=10 starting at x=5 y=6.'''

        rectangle_instance = Rectangle(12, 10, 3)
        expected_output = "[Rectangle] (3) 3/0 - 12/10"
        self.assertEqual(str(rectangle_instance), expected_output)

    def test_str_of_rectangle_12_10_with_x_and_y(self):
        '''12 10'''

        rectangle_instance = Rectangle(12, 10, 3, 6)
        expected_output = "[Rectangle] (4) 3/6 - 12/10"
        self.assertEqual(str(rectangle_instance), expected_output)

    def test_str_of_rectangle_12_10_with_x_y_and_id(self):
        '''12 10'''
        
        rectangle_instance = Rectangle(12, 10, 3, 6, 8)
        expected_output = "[Rectangle] (8) 3/6 - 12/10"
        self.assertEqual(str(rectangle_instance), expected_output)

if __name__ == '__main__':
    unittest.main()