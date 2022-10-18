#!/urs/bin/python3
"""A function that divides all elements of a matrix. """


def matrix_divided(matrix, div):
""" matrix_divided is a function that divids elements      of a matrix it takes as argument bu the second argument
    Args:
        matrix a list of lists of equal len 
        div the number used to divid through the matrix"""


    if type(div) is not int or type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    len_rows = []
    row_count = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        len_rows.append(len(row))
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        row_count += 1
    if len(set(len_rows)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    new_matrix = list(map(lambda row:
                          list(map(lambda x: round(x/div, 2), row)), matrix))
    return new_matrix
