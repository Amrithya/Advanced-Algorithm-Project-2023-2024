# Genetic Algorithm Module

## Introduction
This module is part of a larger project aimed at solving optimization problems using the Genetic Algorithm, a heuristic inspired by the process of natural evolution. This particular implementation focuses on the Matrix Maximum Segment Sum Problem in 2D arrays.

## Features
- `genetic_algorithm_no_constraint.py`: Solves optimization problems without specific constraints.
- `genetic_algorithm_with_constraint.py`: Tailored to handle optimization problems with predefined constraints.

## Problem Description
The Genetic Algorithm implemented here is designed to find a submatrix in a 2D array such that the sum of its elements is maximized. It's an excellent approach for problems that require a balance between exploration and exploitation.

## Installation
Ensure Python 3.x is installed. Clone this repository and navigate to the `genetic_algorithm` directory. Dependencies, if any, should be installed as per the requirements specified in the project's root.

## Usage
To use these algorithms, import the desired module and pass the matrix data as input. For example:

```python
from genetic_algorithm_no_constraint import max_segment_2d_genetic

# Example data
matrix = [[...]]

# Execute the algorithm
result = max_segment_2d_genetic(matrix)
