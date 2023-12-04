# -*- coding: utf-8 -*-

# Function to find the maximum submatrix sum without any constraints
def maxMatrixSum_non_constraint(matrix):
    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Calculate cumulative sums for efficient submatrix sum computation
    cumulative_sums = [[0] * (cols + 1) for _ in range(rows + 1)]
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            cumulative_sums[i][j] = (
                matrix[i - 1][j - 1]
                + cumulative_sums[i - 1][j]
                + cumulative_sums[i][j - 1]
                - cumulative_sums[i - 1][j - 1]
            )

    # Initialize variables to store the maximum sum and corresponding indices
    max_sum = float('-inf')
    top, left, bottom, right = 0, 0, 0, 0

    # Iterate through all possible submatrices to find the maximum sum
    for i1 in range(1, rows + 1):
        for j1 in range(1, cols + 1):
            for i2 in range(i1, rows + 1):
                for j2 in range(j1, cols + 1):
                    # Compute the sum of the current submatrix using cumulative sums
                    submatrix_sum = (
                        cumulative_sums[i2][j2]
                        - cumulative_sums[i1 - 1][j2]
                        - cumulative_sums[i2][j1 - 1]
                        + cumulative_sums[i1 - 1][j1 - 1]
                    )

                    # Update max_sum and corresponding indices if a greater sum is found
                    if submatrix_sum > max_sum:
                        max_sum = submatrix_sum
                        top = i1 - 1
                        left = j1 - 1
                        bottom = i2 - 1
                        right = j2 - 1

    # Return the maximum sum and the indices of the corresponding submatrix
    return max_sum, (top, left), (bottom, right)


# Function to find the maximum submatrix sum with constraints K and L
def maxMatrixSum_constraint(matrix, K, L):
    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Calculate cumulative sums for efficient submatrix sum computation
    cumulative_sums = [[0] * (cols + 1) for _ in range(rows + 1)]
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            cumulative_sums[i][j] = (
                matrix[i - 1][j - 1]
                + cumulative_sums[i - 1][j]
                + cumulative_sums[i][j - 1]
                - cumulative_sums[i - 1][j - 1]
            )

    # Initialize variables to store the maximum sum and corresponding indices
    max_sum = float('-inf')
    top, left, bottom, right = 0, 0, 0, 0

    # Iterate through submatrices with constraints to find the maximum sum
    for i in range(K, rows + 1):
        for j in range(L, cols + 1):
            # Compute the sum of the current submatrix using cumulative sums
            submatrix_sum = (
                cumulative_sums[i][j]
                - cumulative_sums[i - K][j]
                - cumulative_sums[i][j - L]
                + cumulative_sums[i - K][j - L]
            )

            # Update max_sum and corresponding indices if a greater sum is found
            if submatrix_sum > max_sum:
                max_sum = submatrix_sum
                top = i - K
                bottom = i - 1
                left = j - L
                right = j - 1

    # Return the maximum sum and the indices of the corresponding submatrix
    return max_sum, (top, left), (bottom, right)
