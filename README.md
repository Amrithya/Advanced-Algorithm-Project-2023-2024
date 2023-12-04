# Advanced-Algorithm-Project-2023-2024
This repository is dedicated to solving the Matrix Maximum Segment Problem in a 2-dimensional scenario, commonly known as the Maximum Subarray Problem. Our primary objective is to implement various algorithms for this task and provide a comprehensive experimental analysis of their runtime performance and the quality of results. Explore this repository to access the code, documentation, and data related to our research and implementations.


# Project Repository Usage Guide

This guide explains how to use the repository for running and testing different algorithmic approaches.

## Setup

First, ensure you have the following packages installed by running the following command in your terminal :

```
pip install numpy seaborn matplotlib
```

## Creating a Python File

Create a Python file in the project folder.

## Import Modules

Import the required modules as shown below:

```python
from test_class.test_algorithm import TestAlgorithm
from visualizations.visualize_sns import create_test_result_plots
```

## Choose an Approach

Import the approach you want to try. For example:

```python
from brute.brute_force import brute_force_non_constrained, brute_force_constrained
from greedy.greedy_algorithm import greedy_algorithm_non_constrained
```

## Testing the Algorithm

1. Create an instance of the test class:

```python
test_algorithm_instance = TestAlgorithm()
```

2. To test a specific approach without constraints, use the following pattern:

```python
algorithm_name = "Name of your algorithm"
test_results = test_algorithm_instance.run_algorithm_tests(approach_name_call, algorithm_name)
create_test_result_plots(test_results, algorithm_name)
```

For example, to test the brute force approach without constraints:

```python
algorithm_name = "Brute Force Non-Constrained Algorithm"
test_results = test_algorithm_instance.run_algorithm_tests(brute_force_non_constrained, algorithm_name)
create_test_result_plots(test_results, algorithm_name)
```

## Testing with Constraints

1. To test an approach with constraints, add a new parameter `constrained_type` in the `run_algorithm_tests` function. It accepts two string values: 'variable' or 'fixed'.

- `fixed`: Tests the approach against fixed constraints with increasing sizes of arrays.
- `variable`: Tests the approach against variable constraints with a fixed sized array.

Example for fixed constraints:

```python
algorithm_name = "Brute Force Constrained"
test_results = test_algorithm_instance.run_algorithm_tests(brute_force_constrained, algorithm_name, constrained_type='fixed')
create_test_result_plots(test_results, algorithm_name)
```

Example for variable constraints:

```python
test_results = test_algorithm_instance.run_algorithm_tests(brute_force_constrained, algorithm_name, constrained_type='variable')
create_test_result_plots(test_results, algorithm_name)
```
