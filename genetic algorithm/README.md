# Advanced-Algorithm-Project-2023-2024
This repository is dedicated to solving the Matrix Maximum Segment Problem in a 2-dimensional scenario, commonly known as the Maximum Subarray Problem. Our primary objective is to implement various algorithms for this task and provide a comprehensive experimental analysis of their runtime performance and the quality of results. Explore this repository to access the code, documentation, and data related to our research and implementations.

# Matrix Maximum Segment Problem - Genetic Algorithm

This repository contains Python code for solving the Matrix Maximum Segment Problem in a 2-dimensional scenario using a genetic algorithm. The primary goal is to find the submatrix with the maximum sum of elements.

## Overview

- `genetic_algorithm.py`: Python script implementing the genetic algorithm.
- `main.py`: Main script upcoming feature applying the genetic algorithm to a list of test cases.
- `README.md`: This file providing an overview of the project.


## Running the Genetic Algorithm

To execute the genetic algorithm and observe its performance on different test cases, follow the steps below:

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. "Execute" python genetic_algorithm.py


## Usage

This addition explains how to run the genetic algorithm script (`genetic_algorithm.py`) for the current set of test cases and hints at the upcoming feature of running all tests using the `main.py` script.



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

