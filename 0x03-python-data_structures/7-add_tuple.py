#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    '''func that adds tuples'''
    y = check_tuple(tuple_a)
    x = check_tuple(tuple_b)

    if len(y) == 0:
        y = (0, 0)
    if len(x) == 0:
        x = (0, 0)
    add = (y[0] + x[0], y[1] + x[1])

    return(add)
    
def check_tuple(tuple_check=()):
    '''func to check tuple'''

    if len(tuple_check) < 2:
        y = (0, 0)
        tuple_check += y
        return tuple_check
    elif len(tuple_check) > 2:
        new_tuple_check = tuple_check[0:2]
        return new_tuple_check
    elif tuple_check == ():
        return (0, 0)
    else:
        return tuple_check
