#!/usr/bin/python3
# models/base.py
'''Module for Base class.'''

from models.rectangle import Rectangle

class Square(Rectangle):
    '''Class Square inhirit Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''constructor'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''Getter for the size attribute.'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setter for the size attribute.'''
        self.width = value
        self.height = value
    
    def __str__(self):
        '''Return a string representation of the Square.'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"