#!/usr/bin/python3
'''Module for Rectangle class.'''
# models/rectangle.py
from models.base import Base

class Rectangle(Base):
    '''Rectangle class inhirite from Base class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructor: call of the parent construct'''

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Width getter of this rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Width setter of this rectangle.'''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''height getter of this rectangle.'''

        return self.__height

    @height.setter
    def height(self, value):
        '''height setter of this rectangle.'''

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''x'''

        return self.__x

    @x.setter
    def x(self, value):
        '''x setter'''

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''y'''

        return self.__y

    @y.setter
    def y(self, value):
        '''y setter'''
        
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Return the area of the Rectangle.'''
        return self.__width * self.__height
    
    def display(self):
        '''Print the Rectangle instance with the character #.'''
        for _ in range(self.__height):
            print("#" * self.__width)
    
    def to_dictionary(self):
        '''Return the dictionary representation of the Rectangle.'''
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
    
    def __str__(self):
        '''Return a string representation of the Rectangle.'''
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        '''Assign arguments to attributes using both positional and keyworded arguments.'''
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)