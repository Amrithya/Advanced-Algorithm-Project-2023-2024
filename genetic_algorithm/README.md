# Advanced-Algorithm-Project-2023-2024
This repository is dedicated to solving the Matrix Maximum Segment Problem in a 2-dimensional scenario, commonly known as the Maximum Subarray Problem. Our primary objective is to implement various algorithms for this task and provide a comprehensive experimental analysis of their runtime performance and the quality of results. Explore this repository to access the code, documentation, and data related to our research and implementations.

<<<<<<< HEAD
# Matrix Maximum Segment Sum Problem in 2D Arrays - Genetic Algorithm

This repository contains Python code for solving the Matrix Maximum Segment Problem in a 2-dimensional scenario using a genetic algorithm. The primary goal is to find the submatrix with the maximum sum of elements.

### Problem Description
The problem at hand involves finding the contiguous segment with the largest sum within a given two-dimensional array A of size MxN.

### Genetic Algorithm Approach
The genetic algorithm implemented in this project aims to address the Maximum Segment Sum problem in 2D arrays. The formulation is as follows:

### 1.1 Problem Description

#### 1.1.1 Formulation
Given a 2-D array A of size MxN with integers, the task is to find the indices i1, i2, j1, j2 
where 1 <= i1 <= i2 <= M, 1 <= j1 <= j2 <= N such that the sum of the submatrix 
A[x, y] for i1 <= x <= i2, j1 <= y <= j2 is as large as possible.

#### 1.1.2 Constraints
- The array A has dimensions MxN.
- The indices must satisfy 1 <= i1 <= i2 <= M, 1 <= j1 <= j2 <= N.
- The submatrix size is constrained by i2 - i1 + 1 = K and j2 - j1 + 1 = L.
  
Such that the sum Σ_{x=i1}^{i2} Σ_{y=j1}^{j2} A[x, y] is as large as possible. In simple terms, find the subarray of size KxL with the maximum sum possible.

#### Example
For the 2-D array A, the goal is to identify the maximum contiguous segment with the largest sum.



#### Genetic Algorithm Execution
The genetic algorithm is employed to iteratively search for a combination of indices that maximizes the sum of the submatrix within the given constraints. Here's a brief overview of the algorithm's workflow:

1. **Initialization**: Random programs (candidate solutions) are generated, each representing a potential submatrix with specific indices.

2. **Fitness Evaluation**: The fitness of each program is assessed by calculating the sum of the corresponding submatrix.

3. **Selection**: Programs with higher fitness are favored for the next generation. This mimics the survival of the fittest principle.

4. **Recombination and Mutation**: Pairs of programs are combined through recombination, and slight modifications are introduced through mutation to explore the solution space.

5. **Repeat**: Steps 2-4 are repeated for multiple generations to refine the solutions.

6. **Result**: The algorithm converges to a solution, providing the indices `i_1, i_2, j_1, j_2` that yield the maximum segment sum.

## Overview

- `genetic.py`: Python script implementing the genetic algorithm.
- `main.py`: Main script upcoming feature applying the genetic algorithm to a list of test cases.
- `README.md`: This file providing an overview of the project.


## Running the Genetic Algorithm

To execute the genetic algorithm and observe its performance on different test cases, follow the steps below:

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. "Execute" python genetic.py


## Usage

To observe the algorithm in action and assess its performance, run the genetic algorithm script (`genetic.py`). The script currently includes various test cases, each representing different scenarios for the 2D array.This addition explains how to run the genetic algorithm script (`genetic.py`) for the current set of test casesa and stay tuned for further updates, as all test cases will soon be integrated into the `main.py` script for a more comprehensive evaluation of the algorithm's capabilities.


## Test Cases


The genetic algorithm is tested on a variety of 2-dimensional matrices. Each test case is represented as a Python dictionary in the `tests` list in the `main.py` script. Here's an explanation of the test cases:

1. **Test Case 1**

   Matrix:
[
[1, 2, -1, -4, -20],
[-8, -3, 4, 2, 1],
[3, 8, 10, 1, 3],
[-4, -1, 1, 7, -6],
]

Description: This matrix includes both positive and negative values and serves as a general test case for the genetic algorithm.

2. **Test Case 2**

Matrix:
[
[1, 2, -1, -4, -20],
[-8, -3, 4, 2, 1],
[3, 8, 10, 1, 3],
[-4, -1, 1, 7, -6],
]

Description: Similar to Test Case 1, this matrix provides a different configuration of values to test the algorithm's robustness.

3. **Test Case 3**

Matrix:
[
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
]

Description: A smaller matrix with positive integer values, used to test the algorithm's performance on simpler cases.

4. **Test Case 4**

Matrix:
[
[-1, -2, -3],
[-4, -5, -6],
[-7, -8, -9],
]

Description: Similar to Test Case 3, but with negative integer values.

5. **Test Case 5**

Matrix:
[
[1, -2, 3],
[4, -5, 6],
[7, -8, 9],
]

Description: A matrix with a mix of positive and negative values to test the algorithm's handling of different scenarios.

6. **Test Case 6**

Matrix:
[
[1, 2],
[3, 4],
]

Description: A small matrix to test the algorithm's performance on minimal input.

7. **Test Case 7**

Matrix:
[
[2, -1, 4, -6, 2],
[-3, 2, -1, 4, -3],
[1, -5, 2, -1, 5],
[4, -2, 3, 7, -2],
]

Description: A larger matrix with a mix of positive and negative values to assess the algorithm's scalability.

8. **Test Case 8**

Matrix:
[
[-2, 5, -1, 4],
[8, -6, 3, 1],
[2, 2, -4, -1],
[-3, 2, 6, -1],
]

Description: Another matrix with varying positive and negative values.

9. **Test Case 9**

Matrix:
[
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[10, 11, 12],
]

Description: A larger matrix to test the algorithm's scalability.

10. **Test Case 10**

 Matrix:

 [
     [-1, -2, -3],
     [-4, -5, -6],
     [-7, -8, -9],
     [-10, -11, -12],
 ]


 Description: Another larger matrix with negative values.

11. **Test Case 11 to 20**

 Similar to the first 10 test cases, these additional cases cover a range of matrix configurations and sizes.

12. **Test Case 21**

 Matrix:

 [
     [1, 1],
     [1, 1],
     [1, 1],
     [1, 1],
 ]
 
 Description: A matrix with all positive values, used to test the algorithm's behavior in a uniform positive scenario.
=======
# Matrix Maximum Segment Sum Problem in 2D Arrays - Ant Colony Approach
>>>>>>> 0e92023c3c9c65c7a80af7baf0e72fe417f31173
