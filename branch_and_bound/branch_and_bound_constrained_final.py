#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
from collections import deque

def valid(child, m, n):
    if child[1] == 0:
        child[1] = m
    if child[3] == 0:
        child[3] = n
    if ((child[0] < child[1])  or (child[2] < child[3])):
        return True

def generate_children(node, m, n):
    children = []

    for i in range(4):
        if node[i] != 0:
            continue

        for j in range(1, (m if i < 2 else n) + 1):
            child = node.copy()
            child[i] = j
            if valid(child):
                children.append(child)
        break
    return children

def adjust(child, matrix):
    child[0] = child[0] if child[0] != 0 else 1
    child[1] = child[1] if child[1] != 0 else matrix.shape[0]
    child[2] = child[2] if child[2] != 0 else 1
    child[3] = child[3] if child[3] != 0 else matrix.shape[1]
    return child

def bound(child, matrix):
    i1, i2, j1, j2 = child

    i1 = 1 if i1 == 0 else i1
    i2 = matrix.shape[0] if i2 == 0 else i2
    j1 = 1 if j1 == 0 else j1
    j2 = matrix.shape[1] if j2 == 0 else j2

    sub = input_matrix[i1-1:i2, j1-1:j2]
    positive_values = sub[sub > 0]
    up_bound = np.sum(positive_values)
    child_sum = np.sum(sub)

    return (up_bound, child_sum)

def max_segment_branch_and_bound_constrained(matrix, k, l):
    matrix = np.asarray(matrix)
    m, n = matrix.shape
    max_sum = -np.inf
    max_sum_submatrix = None
    initial_indices = [0,0,0,0]
    
    q = deque()
    q.append(initial_indices)

    n = 4
    for i in range (n):
        while q:
            node = q.popleft()
            for child in generate_children(node, m, n):
                up_bound, child_sum = bound(child, matrix)
                if up_bound >= max_sum:
                    q.append(child)
                    if child_sum > max_sum and ((m if child[1] == 0 else child[1]) - child[0] + 1 == k) and ((n if child[3] == 0 else child[3]) - child[2] + 1 == l):
                        max_sum = child_sum
                        max_sum_submatrix = child

    final_indices = adjust(max_sum_submatrix, matrix)
    final_indices = [i - 1 for i in final_indices]
    i1, i2, j1, j2 = final_indices
    max_submatrix = matrix[i1-1:i2, j1-1:j2]
    
    return(max_sum, (i1, j1), (i2, j2))

