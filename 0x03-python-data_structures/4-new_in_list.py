#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    '''func that replace elmnt in list'''
    if idx < 0:
        return
    if idx > len(my_list):
        return
    else:
        new_list = my_list[:]
        new_list[idx] = element
        return new_list
