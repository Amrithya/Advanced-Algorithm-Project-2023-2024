'''
Meryem Ben yahia - MLDM 2023-2025
Randomized Approach Constrained
'''

import random

# Function to find the submatrix with the maximum sum of a fixed size (K x L) in a given matrix
def random_fixed_size_submatrix_sum(matrix, K, L):
    M, N = len(matrix), len(matrix[0]) # Dimensions of the input matrix
    # Calculate the number of iterations based on matrix dimensions
    num_iterations= int((M*(M+1)*N*(N*1))/4) 
    max_sum = float('-inf') # Initialize maximum sum as negative infinity
    best_submatrix = None # Initialize best submatrix as None

    for _ in range(num_iterations):
        # Randomly choose the top-left corner of the submatrix
        i1 = random.randint(0, M - K)
        j1 = random.randint(0, N - L)
        # Calculate the bottom-right corner based on the top-left corner and submatrix size
        i2 = i1 + K - 1
        j2 = j1 + L - 1

        # Compute the sum of elements in the current submatrix
        current_sum = sum(matrix[i][j] for i in range(i1, i2 + 1) for j in range(j1, j2 + 1))

        # Update maximum sum and best submatrix if a better one is found
        if current_sum > max_sum:
            max_sum = current_sum
            best_submatrix = ((i1, j1), (i2, j2))

    # Return the maximum sum and the coordinates of the best submatrix
    return max_sum, best_submatrix[0], best_submatrix[1]
