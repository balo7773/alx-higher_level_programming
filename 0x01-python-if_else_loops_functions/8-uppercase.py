#!/usr/bin/python3
def uppercase(str):
    '''a function to change str to uppercase'''
    for char in str:
        char = ord(char)
        if char >= 97 and char <= 122:
            char = char - 32
        print("{:c}".format(char), end='')
    print("{}".format(""))
