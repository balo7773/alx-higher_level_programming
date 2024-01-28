#!/usr/bin/python3

"""Definning a Square"""

class Square:
    """suare class"""

    def __init__(self, size=0):
        """attribute size
        Args:
            size (int): size of square
        """
    
    @property
    def size(self):
        """getting attribute without init func
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """method(finding area) for square class"""
        return self.__size * self.__size