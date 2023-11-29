def uppercase(str):
    '''a function to change str to uppercase'''
    new_str = ""
    for char in str:
        if 'a' <= char <= 'z':
            new_str += chr(ord(char) - 32)
        else:
            new_str += char
    print(new_str)
