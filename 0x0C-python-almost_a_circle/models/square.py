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
    
    def update(self, *args, **kwargs):
        '''Assign attributes using both positional and keyworded arguments.'''

        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
    def to_dictionary(self):
        '''Return the dictionary representation of the Square.'''
        
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
    
    def __str__(self):
        '''Return a string representation of the Square.'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"