#!/usr/bin/python3
'''Module for Base unit tests.'''
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    '''Tests the Base class.'''

    def test_create_instance_without_id(self):
        '''Test create an instance of Base without passing an id'''

        base = Base()
        self.assertEqual(str(type(base)), "<class 'models.base.Base'>")

    def test_create_instance_with_id(self):
        '''Test if can create an instance of Base with passing an id'''

        base = Base(id=3)
        self.assertEqual(base.id, 3)
    
    def test_auto_id_assigning(self):
        '''Test auto-assignment of id when creating instance'''

        base = Base()
        self.assertIsNotNone(base.id)

    def test_auto_id_incrementation(self):
        '''Test that ids are incremented correctly'''

        base1 = Base()
        base2 = Base()
        self.assertEqual(base2.id, base1.id+1)
    
    def test_base_has_static_method_to_json_string(self):
        '''Test static method to json string in Base class'''

        self.assertTrue(hasattr(Base, "to_json_string"))
        self.assertTrue(callable(getattr(Base, "to_json_string", None)))

    def test_to_json_string_returns_string(self):
        '''Test returns a string from to_json_string'''

        result = Base.to_json_string([])
        self.assertIsInstance(result, str)

    def test_to_json_string_returns_empty_list_string_if_none(self):
        '''Test returns empty list string if none is passed'''

        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_returns_empty_list_string_if_empty_list(self):
        '''Test returns empty list string if empty list is passed'''

        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_returns_json_representation_of_list(self):
        '''Test returns json representation of list if valid list is passed'''

        rectangle_instance = Rectangle(5, 4, 2, 3, 1)
        result = Base.to_json_string([rectangle_instance.to_dictionary()])
        expected = '[{"id": 1, "width": 5, "height": 4, "x": 2, "y": 3}]'
        self.assertEqual(result, expected)

    def test_to_json_string_returns_json_representation_of_list_with_square(self):
        '''Test returns json representation of list with square if valid list is passed'''

        square_instance = Square(5, 2, 3, 1)
        result = Base.to_json_string([square_instance.to_dictionary()])
        expected = '[{"id": 1, "size": 5, "x": 2, "y": 3}]'
        self.assertEqual(result, expected)

    def test_to_json_string_returns_json_representation_of_list_with_other_objects(self):
        '''Test returns json representation of list with other objects if valid list is passed'''

        other_instance = Base()
        result = Base.to_json_string([other_instance.to_dictionary()])
        expected = '[{"id": 1}]'
        self.assertEqual(result, expected)

    def test_to_json_string_returns_json_representation_of_list_with_mixed_objects(self):
        '''Test returns json representation of list with mixed objects if valid list is passed'''
        
        rectangle_instance = Rectangle(5, 4, 2, 3, 1)
        square_instance = Square(5, 2, 3, 2)
        result = Base.to_json_string([rectangle_instance.to_dictionary(), square_instance.to_dictionary()])
        expected = '[{"id": 1, "width": 5, "height": 4, "x": 2, "y": 3}, {"id": 2, "size": 5, "x": 2, "y": 3}]'
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
