#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    '''func to ptint matrix'''
    for i in matrix:
        for j in i:
            if j == i[-1]:
                print("{:d}".format(j))
            else:
                print("{:d}".format(j), end=' ')
    print()
