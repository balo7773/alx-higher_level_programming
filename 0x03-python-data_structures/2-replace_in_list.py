#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    ''' func that replace elmnt in list'''
    if idx < 0:
        return
    if idx > len(my_list):
        return
    else:
        my_list[idx] = element
        return my_list
    