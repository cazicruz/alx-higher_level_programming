#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy_matrix = [value**2 for row in matrix for value in row]

    return copy_matrix
