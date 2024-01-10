#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
        func that returns matrix suare
    """
    return [list(map(lambda i: i*i, row)) for row in matrix]
