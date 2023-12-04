# Greedy Algorithm Functions
This folder  is dedicated to solving the Matrix Maximum Segment Problem in a 2-dimensional scenario, commonly known as the Maximum Subarray Problem, using Greedy approach. 
#### Overview
This document provides an overview and usage guide for implementing greedy algorithm

### Function 
**greedy_algorithm_non_constrained(matrix)**
   - **Description**: Applies a greedy approach to find the maximum subarray sum in a 2D array by transforming it into a 1D problem.
   - **Inputs**:
     - `matrix` (list of lists): A 2D array of numbers, which can include both positive and negative integers.
   - **Outputs**:
     - A tuple containing:
       - Maximum subarray sum (int).
       - A tuple of the start row and column indices (int, int) of the subarray.
       - A tuple of the end row and column indices (int, int) of the subarray.

#### Usage Example
```python
from your_module import greedy_algorithm_non_constrained


# Example for 2D array
matrix = [
    [1, -2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]
max_sum_2d, top_left, bottom_right = greedy_algorithm_non_constrained(matrix)
print(f"Maximum sum: {max_sum_2d}, Submatrix Top-Left: {top_left}, Bottom-Right: {bottom_right}")
```

#### Installation

To use this  function, include the Python module in your project and import the function as shown in the usage example.