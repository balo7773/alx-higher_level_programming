#!/usr/bin/python3
"""
    This program contains a function matrix_mul(a, b) that
    multiplies 2 matrices. if a or b is not a trix, a TypeError
    is raised.
"""


def matrix_mul(m_a, m_b):
    """ Multiplies a matrix """

    msg = ["m_a", "m_b"]
    matrix = [m_a, m_b]
    for i in range(2):
        if type(matrix[i]) is not list:
            raise TypeError("{} must be a list"
                            .format(msg[i]))

    for i in range(2):
        for k in matrix[i]:
            if type(k) is not list:
                raise TypeError("{} must be a list of lists"
                                .format(msg[i]))

    for i in range(2):
        if len(matrix[i]) == 0:
            raise ValueError("{} can't be empty".format(msg[i]))

        for k in matrix[i]:
            if len(k) == 0:
                raise ValueError("{} can't be empty".format(msg[i]))

    for i in range(2):
        for k in matrix[i]:
            for elmnt in k:
                if type(elmnt) is not int and type(elmnt) is not float:
                    raise TypeError("{} should contain only"
                                    " integers or floats"
                                    .format(msg[i]))

    for i in range(2):
        matrix = matrix[i]
        row_size = len(matrix[0])
        for j in range(1, len(matrix)):
            if len(matrix[j]) != row_size:
                raise TypeError("each row of {} must be "
                                "of the same size"
                                .format(msg[i]))

    m_a_col_size = len(m_a[0])
    m_b_row_size = len(m_b)
    if m_a_col_size != m_b_row_size:
        raise ValueError("m_a and m_b can't be multiplied")

    matrix_mul = []
    for row in m_a:
        mat_row = []
        for j in range(len(m_b[0])):
            mul_sum = 0
            for i in range(m_a_col_size):
                mul_sum += row[i] * m_b[i][j]
            mat_row.append(mul_sum)
        matrix_mul.append(mat_row)

    return matrix_mul
