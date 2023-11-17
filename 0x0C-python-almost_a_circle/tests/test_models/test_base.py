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

if __name__ == '__main__':
    unittest.main()
