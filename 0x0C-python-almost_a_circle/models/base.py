#!/usr/bin/python3
# models/base.py
'''Module for Base class.'''
import json

class Base:
    '''A representation of the base of our OOP hierarchy.'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor.'''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        '''Return the JSON string representation of list_dictionaries.'''
        
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
