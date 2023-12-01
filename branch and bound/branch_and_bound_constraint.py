# -*- coding: utf-8 -*-
"""Branch and Bound Constraint.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EsoylFMRo4uZxRhhDOwW3UbAtaAx4qpU
"""

import numpy as np
from collections import deque

def positive_sum(matrix):
    s= 0
    for row in matrix:
        for i in row:
            if i > 0:
                s += i

    return s


def max_segment_branch_and_bound_constraint(matrix, k, l):
    m = matrix.shape[0]
    n = matrix.shape[1]
    initial_partial = ([0, m-1, 0, n-1], np.sum(matrix))
    initial_best = positive_sum(matrix)

    def valid(i1, i2, j1, j2):
        return i1 <= i2 and j1 <= j2 and i1 >= 0 and i2 < m and j1 >= 0 and j2 < n

    def matrix_sub_sum(i1, i2, j1, j2):
        return np.sum(matrix[i1:i2+1, j1:j2+1])

    def positive_sub_sum(i1, i2, j1, j2):
        s = 0
        for i in range(i1, i2+1):
            for j in range(j1, j2+1):
                if matrix[i, j] > 0:
                    s += matrix[i, j]
        return s

    def generate_children(partial, best):
        i1, i2, j1, j2 = partial[0]
        children = []

        if valid(i1+1, i2, j1, j2):
            children.append([((i1+1, i2, j1, j2), matrix_sub_sum(i1+1, i2, j1, j2)), positive_sub_sum(i1+1, i2, j1, j2)])

        if valid(i1, i2-1, j1, j2):
            children.append([((i1, i2-1, j1, j2), matrix_sub_sum(i1, i2-1, j1, j2)), positive_sub_sum(i1, i2-1, j1, j2)])

        if valid(i1, i2, j1+1, j2):
            children.append([((i1, i2, j1+1, j2), matrix_sub_sum(i1, i2, j1+1, j2)), positive_sub_sum(i1, i2, j1+1, j2)])

        if valid(i1, i2, j1, j2-1):
            children.append([((i1, i2, j1, j2-1), matrix_sub_sum(i1, i2, j1, j2-1)), positive_sub_sum(i1, i2, j1, j2-1)])
        return children

    q = deque([(initial_partial, initial_best)])

    while q:
        current_partial, current_best = q.popleft()

        for child in generate_children(current_partial, current_best):
            if child[1] > initial_partial[1]:
                q.append(child)
                if child[0][1] > initial_partial[1] and (child[0][0][1] - child[0][0][0] + 1 == k) and (child[0][0][3] - child[0][0][2] + 1 == l):
                    initial_partial = child[0]


    return initial_partial[1] , (initial_partial[0][0] + 1, initial_partial[0][2] + 1) ,(initial_partial[0][1] + 1,initial_partial[0][3] + 1)