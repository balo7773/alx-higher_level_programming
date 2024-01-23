#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    no = 0
    try:
        for index in range(x):
            print(my_list[index], end='')
            no += 1
    except IndexError:
        None
    print()
    return no
