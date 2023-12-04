# Brute Force Algorithm for Matrix Maximum Segment Problem

This module, `brute_force`, is dedicated to solving the Matrix Maximum Segment Problem in a 2-dimensional scenario, commonly known as the Maximum Subarray Problem, using a brute force approach.

#### Overview

This document provides an overview and usage guide for implementing the brute force algorithm contained and unconstrained within this module.

### Functions

**brute_force_non_constrained(matrix)**
   - **Description**: Applies brute force approach to find the maximum subarraysum in a 2D array
   - **Arguments**:
       - `matrix`: A 2D array (list) of numbers.
   - **Returns**:
       - A tuple containing:
           - The maximum subarray sum (int).
           - A tuple of the start row and column indices (int, int) of the subarray.
           - A tuple of the end row and column indices (int, int) of the subarray.

### Usage

To use this function, import it from the `brute_force` module and pass a 2D array as the argument.

 For example:

```python
from your_module_name import brute_force_non_constrained

matrix = [[...]]  # Replace with your 2D array
result = brute_force_non_constrained(matrix)
print(result)
```

**brute_force_constrained(matrix,k,l)**
   - **Description**: Applies brute force approach to find the maximum subarraysum in a 2D array with k and l constraints
   - **Arguments**:
       - `matrix`: A 2D array (list) of numbers.
       - `k` : (int) number of rows constraints
       - `l` : (int) number of columns constraints

   - **Returns**:
       - A tuple containing:
           - The maximum subarray sum (int).
           - A tuple of the start row and column indices (int, int) of the subarray.
           - A tuple of the end row and column indices (int, int) of the subarray.

### Usage

To use this function, import it from the `brute_force` module and pass a 2D array , k, and l as the arguments .

 For example:

```python
from your_module_name import brute_force_constrained

matrix = [[...]]  # Replace with your 2D array
result = brute_force_constrained(matrix,k,l)
print(result)
```


#### Installation

To use this  function
- include the Python module in your project and import the function as shown in the usage example.
-**make sure you have helpers.py in the same folder as your brute.force module**

