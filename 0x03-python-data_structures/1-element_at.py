#!/usr/bin/python3
def element_at(my_list, idx):
    '''a func to retrieve elmnt from a list'''
    if idx < 0:
        return None
    if idx > len(my_list):
        return None
    else:
        element = my_list[idx]
    return element
