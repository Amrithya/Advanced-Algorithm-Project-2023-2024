# Advanced-Algorithm-Project-2023-2024
This repository is dedicated to solving the Matrix Maximum Segment Problem in a 2-dimensional scenario, commonly known as the Maximum Subarray Problem. Our primary objective is to implement various algorithms for this task and provide a comprehensive experimental analysis of their runtime performance and the quality of results. Explore this repository to access the code, documentation, and data related to our research and implementations.

# Dynamic programming 

## Introduction

The provided Python functions, `maxMatrixSum_non_constraint` and `maxMatrixSum_constraint`, aim to efficiently find the maximum submatrix sum in a given matrix. The `maxMatrixSum_non_constraint` function works without any constraints, while the `maxMatrixSum_constraint` function considers constraints K and L.

## 1. Functions

### 1.1  `maxMatrixSum_non_constraint(matrix)`

This function takes a 2D matrix as input and returns a tuple containing the maximum submatrix sum and the indices of the corresponding submatrix.

```python
max_sum, top_left, bottom_right = maxMatrixSum_non_constraint(matrix)
```

1. matrix: The input 2D matrix.

2. max_sum: The maximum submatrix sum.

3. top_left: Tuple containing the row and column indices of the top-left corner of the submatrix.

4. bottom_right: Tuple containing the row and column indices of the bottom-right corner of the submatrix.

### 1.2 `maxMatrixSum_constraint(matrix, K, L)`
This function takes a 2D matrix and two constraints, K and L, as input and returns a tuple containing the maximum submatrix sum and the indices of the corresponding submatrix with constraints.

```python
max_sum, top_left, bottom_right = maxMatrixSum_constraint(matrix, K, L)
```

1. matrix: The input 2D matrix.

2. K: Constraint representing the maximum number of rows in the submatrix.

3. L: Constraint representing the maximum number of columns in the submatrix.

4. max_sum: The maximum submatrix sum.

5. top_left: Tuple containing the row and column indices of the top-left corner of the submatrix.

6. bottom_right: Tuple containing the row and column indices of the bottom-right corner of the submatrix.

## 2. Usage 

The functions are imported in the main_dynamic which is used to call these functions and is used of visualizations and comparsion between various algorithms.

```python
from dynamic_programming.dynamic_programming import maxMatrixSum_non_constraint,maxMatrixSum_constraint
from test_class.test_algorithm import TestAlgorithm
from visualizations.visualize_sns import create_test_result_plots
import numpy as np
import timeit
```
 
 Import and install all packages

```python
pip install seaborn
pip install matplotlib
```

