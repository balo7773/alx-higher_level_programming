#!/usr/bin/pytho3
def square_matrix_map(matrix=[]):
    return list(map(lambda i: list(map(lambda j: j**2, i)), matrix))