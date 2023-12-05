#!/usr/bin/python3

def max_integer(my_list=[]):
    '''func to find max no'''
    if not my_list:
        return None
    else:
        max = my_list[0]
        for i in range(1, len(my_list)):
            if max - my_list[i] < 0:
                max = my_list[i]
    return max
