#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    '''multiply dictionary keys by 2'''
    for i in a_dictionary:
        a_dictionary[i] *= 2
    return a_dictionary
