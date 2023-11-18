#!/usr/bin/python3
'''Module for Rectangle class.'''
# models/rectangle.py
from models.base import Base

class Rectangle(Base):
    '''Class representing a rectangle inhirite Base class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor.'''
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
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("Width must be greater than zero")
        self.__width = value

    @property
    def height(self):
        '''height getter of this rectangle.'''

        return self.__height

    @height.setter
    def height(self, value):
        '''height setter of this rectangle.'''

        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height must be greater than zero")
        self.__height = value

    @property
    def x(self):
        '''x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Setter for the x coordinate of the top-left corner of the rectangle.'''
        if not isinstance(value, int):
            raise TypeError("X must be an integer")
        if value < 0:
            raise ValueError("X cannot be negative")
        self.__x = value

    @property
    def y(self):
        '''y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Setter for the y coordinate of the top-left corner of the rectangle.'''
        if not isinstance(value, int):
            raise TypeError("Y must be an integer")
        if value < 0:
            raise ValueError("Y cannot be negative")
        self.__y = value
