#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from collections import deque

def valid(child, m, n):
    # Helper function to check if the child indices are valid
    if child[1] == 0:
        child[1] = m
    if child[3] == 0:
        child[3] = n
    if ((child[0] < child[1]) or (child[2] < child[3])):
        return True

def generate_children(node, m, n):
    # Helper function to generate valid child indices based on the current node
    children = []

    for i in range(4):
        if node[i] != 0:
            continue

        for j in range(1, (m if i < 2 else n) + 1):
            child = node.copy()
            child[i] = j
            if valid(child, m, n):
                children.append(child)
        break
    return children

def adjust(child, matrix):
    # Helper function to adjust child indices based on the matrix dimensions
    child[0] = 1 if child[0] == 0 else child[0]
    child[1] = matrix.shape[0] if child[1] == 0 else child[1]
    child[2] = 1 if child[2] == 0 else child[2]
    child[3] = matrix.shape[1] if child[3] == 0 else child[3]
    return child

def bound(child, matrix):
    # Helper function to calculate upper and lower bounds for the child submatrix
    i1, i2, j1, j2 = child

    i1 = 1 if i1 == 0 else i1
    i2 = matrix.shape[0] if i2 == 0 else i2
    j1 = 1 if j1 == 0 else j1
    j2 = matrix.shape[1] if j2 == 0 else j2
    
    sub = matrix[i1-1:i2, j1-1:j2]
    positive_values = sub[sub > 0]
    up_bound = np.sum(positive_values)
    child_sum = np.sum(sub)

    return (up_bound, child_sum)

def max_segment_branch_and_bound(matrix):
    # Convert the input matrix to a NumPy array
    matrix = np.asarray(matrix)
    m, n = matrix.shape
    max_sum = -np.inf
    max_sum_submatrix = None
    indices = [0, 0, 0, 0]
    
    q = deque()
    q.append(indices)

    n_iter = 4
    for i in range(n_iter):
        while q:
            node = q.popleft()
            for child in generate_children(node, m, n):
                up_bound, child_sum = bound(child, matrix)
                if up_bound >= max_sum:
                    q.append(child)
                    if child_sum > max_sum:
                        max_sum = child_sum
                        max_sum_submatrix = child

    # Adjusting indices to get the sub matrix
    final_indices = adjust(max_sum_submatrix, matrix)
    final_indices = [i - 1 for i in final_indices]
    i1, i2, j1, j2 = final_indices
    max_submatrix = matrix[i1-1:i2, j1-1:j2]
    
    return max_sum, (i1, j1), (i2, j2)
