#!/usr/bin/python3
def calcSquare(n):
    return n*n

def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    return list(list(map(calcSquare, num_list)) for num_list in matrix)
