#!/usr/bin/python3
"""
    This program contains a function add_integer(a, b)
    that adds two integers or floats and return the result,
"""


def add_integer(a, b=98):
    """ Adds two integers and returns the result """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return a + b
