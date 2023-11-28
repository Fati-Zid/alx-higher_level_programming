#!/usr/bin/python3
"""
Module for Square class
"""


class Square:
    """
    Defines a square with a private instance attribute size.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size
