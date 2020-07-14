#!/usr/bin/python3
"""
function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):

    """ Args:
        matrix (:obj:`list` of :obj:`list` of :obj:`int` or :obj:`float`):
            list of lists of integers or floats
        div (int or float): divisor
    Returns:
        a new matrix containing the quotients
    Raises:
        TypeError: if matrix elements are neither int nor float,
            if matrix rows are not the same size
        ZeroDivisionError: if dividing by zero
    """
    new_matrix = []

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in range(len(matrix)):
        for element in range(len(matrix[row])):
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
            if len(matrix[0]) != len(matrix[row]):
                raise TypeError("Each row of the matrix must have the"
                                " same size")
    new_matrix = [[round(element / div, 2) for element in row]
                  for row in matrix]
    return new_matrix
