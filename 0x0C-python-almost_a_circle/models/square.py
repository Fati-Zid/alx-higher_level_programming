#!/usr/bin/python3
# models/base.py
'''Module for Base class.'''

from models.rectangle import Rectangle

class Square(Rectangle):
    '''Class Square inhirit Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Return a string representation of the Square.'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"