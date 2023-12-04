# Advanced-Algorithm-Project-2023-2024
## Randomized Approach Constrained `randomized_constrained.py` 
### Function Description
- **Main Function**: `random_fixed_size_submatrix_sum`
- **Input Parameters**:
  - `matrix`: The input matrix (a list of lists) within which the submatrix will be found.
  - `K`: The number of rows in the desired submatrix.
  - `L`: The number of columns in the desired submatrix.
- **Return**: The function returns the maximum sum found within any submatrix of the specified size and the coordinates (top-left and bottom-right corners) of this submatrix.


## Randomized Approach Un-constrained `gradient_unconstrained.py` 

### Function Descriptions
- **calculate_iterations(M, N)**: Determines the number of iterations for the gradient descent process, based on the dimensions of the matrix (`M` and `N`).
- **calculate_trials(M, N)**: Calculates the number of trials to find the maximum sum submatrix, ensuring a comprehensive search.
- **create_cumulative_sum_matrix(matrix)**: Generates a cumulative sum matrix from the input matrix to allow efficient computation of submatrix sums.
- **submatrix_sum(cum_sum_matrix, top_left, bottom_right)**: Computes the sum of elements in a submatrix defined by its top-left and bottom-right corners.
- **gradient_descent_submatrix(cum_sum_matrix, M, N)**: Applies a gradient descent approach to find the submatrix with the maximum sum. It involves randomly initializing the submatrix and iteratively making adjustments (expanding, shrinking, or moving) to maximize the sum.
- **find_max_sum_submatrix(matrix)**: The main function that orchestrates the entire process. It calculates the cumulative sum matrix, then repeatedly applies the gradient descent method over several trials to find the overall best submatrix with the maximum sum.

### Author
Meryem Ben Yahia, MLDM 2023-2025