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

if __name__ == '__main__':
    unittest.main()
