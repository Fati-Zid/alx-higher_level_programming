#!/usr/bin/python3
'''Module for Square unit tests.'''
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base

class TestSquare(unittest.TestCase):
    '''Class to test the square class and its methods.'''

    def test_class_exists(self):
        '''Check if the square class exists.'''

        self.assertTrue(hasattr(Square, "__init__"))
        self.assertTrue(hasattr(Square, "__str__"))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))

    def test_create_square_with_only_size(self):
        '''Create a square with only size attribute.'''

        square_instance = Square(5)
        self.assertEqual(square_instance.size, 5)
        self.assertEqual(square_instance.width, 5)
        self.assertEqual(square_instance.height, 5)

    def test_create_square_with_size_and_x(self):
        '''Create a square with size and x attributes.'''

        square_instance = Square(5, 7)
        self.assertEqual(square_instance.size, 5)
        self.assertEqual(square_instance.width, 5)
        self.assertEqual(square_instance.height, 5)
        self.assertEqual(square_instance.x, 7)

    def test_create_square_with_size_x_and_y(self):
        '''Create a square with size, x and y attributes.'''

        square_instance = Square(5, 7, 2)
        self.assertEqual(square_instance.size, 5)
        self.assertEqual(square_instance.width, 5)
        self.assertEqual(square_instance.height, 5)
        self.assertEqual(square_instance.x, 7)
        self.assertEqual(square_instance.y, 2)

    def test_create_square_with_size_x_y_and_id(self):
        '''Create a square with size, x, y and id attributes.'''

        square_instance = Square(5, 7, 2, 89)
        self.assertEqual(square_instance.size, 5)
        self.assertEqual(square_instance.width, 5)
        self.assertEqual(square_instance.height, 5)
        self.assertEqual(square_instance.x, 7)
        self.assertEqual(square_instance.y, 2)
        self.assertEqual(square_instance.id, 89)

    def test_size_getter_and_setter(self):
        '''Test getters and setters for size attribute of square.'''

        square_instance = Square(10)
        self.assertEqual(square_instance.size, 10)

        square_instance.size = 12
        self.assertEqual(square_instance.size, 12)
        self.assertEqual(square_instance.width, 12)
        self.assertEqual(square_instance.height, 12)

    def test_set_size_with_non_integer_value(self):
        '''Set the size to non-integer value should raise an exception.'''

        square_instance = Square(10)
        with self.assertRaises(TypeError):
            square_instance.size = "invalid"

    def test_set_size_with_non_positive_value(self):
        '''Set the size to non-positive integer value should raise an exception.'''

        square_instance = Square(10)
        with self.assertRaises(ValueError):
            square_instance.size = 0
    
    def test_update_with_args_id(self):
        '''Update square instance using args (size, x, y, id).'''

        square_instance = Square(5)
        square_instance.update(89)
        self.assertEqual(square_instance.id, 89)

    def test_update_with_args_id_and_size(self):
        '''Update square instance using args (size, x, y, id).'''

        square_instance = Square(5)
        square_instance.update(89, 6)
        self.assertEqual(square_instance.id, 89)
        self.assertEqual(square_instance.size, 6)
        self.assertEqual(square_instance.width, 6)
        self.assertEqual(square_instance.height, 6)

    def test_update_with_args_id_size_and_x(self):
        '''Update square instance using args (size, x, y, id).'''

        square_instance = Square(5)
        square_instance.update(89, 6, 2)
        self.assertEqual(square_instance.id, 89)
        self.assertEqual(square_instance.size, 6)
        self.assertEqual(square_instance.width, 6)
        self.assertEqual(square_instance.height, 6)
        self.assertEqual(square_instance.x, 2)

    def test_update_with_args_id_size_x_and_y(self):
        '''Update square instance using args (size, x, y, id).'''

        square_instance = Square(5)
        square_instance.update(89, 6, 2, 3)
        self.assertEqual(square_instance.id, 89)
        self.assertEqual(square_instance.size, 6)
        self.assertEqual(square_instance.width, 6)
        self.assertEqual(square_instance.height, 6)
        self.assertEqual(square_instance.x, 2)
        self.assertEqual(square_instance.y, 3)

    def test_update_with_kwargs_id(self):
        '''Update square instance using kwargs (size=None, x=None, y=None, id).'''

        square_instance = Square(5)
        square_instance.update(id=89)
        self.assertEqual(square_instance.id, 89)

    def test_update_with_kwargs_id_and_size(self):
        '''Update square instance using kwargs (size=None, x=None, y=None, id).'''

        square_instance = Square(5)
        square_instance.update(id=89, size=8)
        self.assertEqual(square_instance.id, 89)
        self.assertEqual(square_instance.size, 8)
        self.assertEqual(square_instance.width, 8)
        self.assertEqual(square_instance.height, 8)

    def test_update_with_kwargs_id_size_and_x(self):
        '''Update square instance using kwargs (size=None, x=None, y=None, id).'''

        square_instance = Square(5)
        square_instance.update(id=89, size=8, x=3)
        self.assertEqual(square_instance.id, 89)
        self.assertEqual(square_instance.size, 8)
        self.assertEqual(square_instance.width, 8)
        self.assertEqual(square_instance.height, 8)
        self.assertEqual(square_instance.x, 3)

    def test_update_with_kwargs_id_size_x_and_y(self):
        '''Update square instance using kwargs (size=None, x=None, y=None, id).'''

        square_instance = Square(5)
        square_instance.update(id=89, size=8, x=3, y=4)
        self.assertEqual(square_instance.id, 89)
        self.assertEqual(square_instance.size, 8)
        self.assertEqual(square_instance.width, 8)
        self.assertEqual(square_instance.height, 8)
        self.assertEqual(square_instance.x, 3)
        self.assertEqual(square_instance.y, 4)

    def test_to_dictionary_returns_dict(self):
        '''Returns dictionary representation of the object.'''

        square_instance = Square(5, 2, 3, 1)
        result = square_instance.to_dictionary()
        self.assertIsInstance(result, dict)

    def test_to_dictionary_returns_dict_with_4_keys(self):
        '''Returns dictionary with four keys: type, width, height and position.'''

        square_instance = Square(5, 2, 3, 1)
        result = square_instance.to_dictionary()
        self.assertEqual(len(result), 4)

    def test_to_dictionary_contains_id(self):
        '''Dictionary contains key "id".'''

        square_instance = Square(5, 2, 3, 1)
        result = square_instance.to_dictionary()
        self.assertIn('id', result)

    def test_to_dictionary_contains_size(self):
        '''Dictionary contains key "size".'''

        square_instance = Square(5, 2, 3, 1)
        result = square_instance.to_dictionary()
        self.assertIn('size', result)

    def test_to_dictionary_contains_x(self):
        '''Dictionary contains key "position" which is a list containing two elements - x and y coordinates.'''

        square_instance = Square(5, 2, 3, 1)
        result = square_instance.to_dictionary()
        self.assertIn('x', result)

    def test_to_dictionary_contains_y(self):
        '''contain y'''
        
        square_instance = Square(5, 2, 3, 1)
        result = square_instance.to_dictionary()
        self.assertIn('y', result)

if __name__ == '__main__':
    unittest.main()