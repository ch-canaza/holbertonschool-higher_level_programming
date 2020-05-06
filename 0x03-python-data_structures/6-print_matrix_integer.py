#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    len_i = len(matrix)
    if not matrix[0]:
        print()
    for i in range(len_i):
        len_j = len(matrix[i])
        for j in range(len_j):
            if j == len_j - 1:
                print("{:d}".format(matrix[i][j]))
            else:
                print("{:d}".format(matrix[i][j]), end="")
