#!/usr/bin/python3
def best_score(a_dictionary):
    '''func that returns biggest key value'''
    if a_dictionary == {}:
        return None
    new_value = 0
    new_key= ""
    for key, value in a_dictionary.items():
        if value > new_value:
            new_value = value
            new_key = key
    return new_key
