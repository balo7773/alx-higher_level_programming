#!/usr/bin/python3

def multiple_returns(sentence):
    '''func that returns first char'''
    if sentence == "":
        return None
    else:
        first = sentence[0]
    return (len(sentence), first)
