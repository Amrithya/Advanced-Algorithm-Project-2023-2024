
from brute.helpers import calculate_subarray_sum,print_submatrix


def brute_force_non_constrained(matrix):
    """
    this function involves fixing a top left corner calculating the sum of every possible sub-array for this fixed
    corner, and then determining which one has the highest sum. This approach is exhaustive and
    considers all potential sub-arrays within the matrix
    
    Args:
    matrix : A 2D array (list) of numbers. 

    Returns:
    tuple: A tuple containing:
           - The first element is the maximum subarray sum (int).
           - The second element is a tuple of the start row and column indices (int, int) of the subarray.
           - The third element is a tuple of the end row and column indices (int, int) of the subarray.
    """


    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    cols =  len(matrix[0])  if rows>0 else 0 
    
    # Initialize variables to store maximum sum and corresponding indices
    max_sum = float('-inf')
    top_left = bottom_right = (0, 0) 

    # Iterate through all possible submatrices
    for top in range(rows):
        for left in range(cols): 
            for bottom in range(top, rows):
                for right in range(left, cols):
                    # Calculate the sum of the current subarray
                    current_sum = calculate_subarray_sum(matrix, top, left, bottom, right)
                    if current_sum > max_sum:
                        max_sum = current_sum
                        top_left = (top, left)
                        bottom_right = (bottom, right)
                    
    return max_sum, top_left, bottom_right,


# BRUTE FORCE CONSTRAINED
"""
    this function is similar to the unconstrained version but with an additional
    check before calculating the sum for if the constraints (k and l) rows and columns
    respectively are withing the boundaries
    
    Args:
    matrix : A 2D array (list) of numbers. 
    k : (int) number of rows constraints
    l : (int) number of columns constraints

    Returns:
    tuple: A tuple containing:
           - The first element is the maximum subarray sum (int).
           - The second element is a tuple of the start row and column indices (int, int) of the subarray.
           - The third element is a tuple of the end row and column indices (int, int) of the subarray.
    """

def brute_force_constrained(matrix,K,L):
    rows, cols = len(matrix), len(matrix[0])
    max_sum = float('-inf')
    top_left = bottom_right = (0, 0)  # Initialize with the first element

    for i in range(rows):# Loop for top row position in the rectangle   
        for j in range(cols): # Loop for left column position of the rectangle
            for k in range(i, rows):# Loop for bottom row in the rectangle
                for l in range(j, cols):# Loop for right column in the rectangle
                    # check  the constraints
                    if (k-i+1 == K and l-j+1 == L):
                        current_sum = calculate_subarray_sum(matrix, i, j, k, l)
                        if current_sum > max_sum:
                            max_sum = current_sum
                            top_left = (i, j)
                            bottom_right = (k, l)

    return max_sum, top_left, bottom_right,










