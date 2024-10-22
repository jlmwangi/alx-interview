#!/usr/bin/python3
"""rotating a 2d matrix"""


def rotate_2d_matrix(matrix):
    """method to rotate matrix
    transpose it first using map
    then reverse the contents in order"""
    trans_matrix = list(map(list, zip(*matrix)))

    for i in range(len(matrix)):
        matrix[i][:] = trans_matrix[i][::-1]
