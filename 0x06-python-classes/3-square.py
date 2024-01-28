#!/usr/bin/python3

"""Definning a Square"""

class Square:
    """suare class"""

    def __init__(self, size=0):
        """attribute size
        Args:
            size (int): size of square
        """
        self.size = size

    @property
    def size(self):
        """The getter method for the size attribute
        """

        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


    def area(self):
        """method(finding area) for square class"""
        return self.__size * self.__size
