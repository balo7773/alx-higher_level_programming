#!/usr/bin/python3
"""
    This program contains a func print_square(size)
    that prints a square with characters # based on size
"""


def print_square(size):
    """ Prints a square with # character """

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
