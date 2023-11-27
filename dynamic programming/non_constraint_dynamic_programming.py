# -*- coding: utf-8 -*-
"""Non-Constraint Dynamic Programming.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IfrGP3mrvZiV_EmAqeSHcZUYC9o50Geu
"""

# Commented out IPython magic to ensure Python compatibility.
!pip install ipython-autotime
# %load_ext autotime

from matplotlib import pyplot as plt
import cProfile
import re
from time import perf_counter

tests = [
    {
        "matrix": [
            [1, 2, -1, -4, -20],
            [-8, -3, 4, 2, 1],
            [3, 8, 10, 1, 3],
            [-4, -1, 1, 7, -6],
        ],
        "expected_result": 29,
        "subarray_indices": [(1, 1), (3, 3)], #top left and bottom right indices
    },

    {
        "matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        "expected_result": 45,
        "subarray_indices": [(0, 0), (2, 2)],
    },
    {
        "matrix": [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]],
        "expected_result": -1,
        "subarray_indices": [(0, 0), (0, 0)],
    },
    {
        "matrix": [[1, -2, 3], [4, -5, 6], [7, -8, 9]],
        "expected_result": 18,
        "subarray_indices": [(0, 2), (2, 2)],
    },
    {
        "matrix": [[1, 2], [3, 4]],
        "expected_result": 10,
        "subarray_indices": [(0, 0), (1, 1)],
    },
    {
        "matrix": [
            [2, -1, 4, -6, 2],
            [-3, 2, -1, 4, -3],
            [1, -5, 2, -1, 5],
            [4, -2, 3, 7, -2],
        ],
        "expected_result": 14,
        "subarray_indices": [(0, 2), (3, 4)],
    },
    {
        "matrix": [[-2, 5, -1, 4], [8, -6, 3, 1], [2, 2, -4, -1], [-3, 2, 6, -1]],
        "expected_result": 15,
        "subarray_indices": [(0, 0), (3, 3)],
    },
    {
        "matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
        "expected_result": 78,
        "subarray_indices": [(0, 0), (3, 2)],
    },
    {
        "matrix": [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9], [-10, -11, -12]],
        "expected_result": -1,
        "subarray_indices": [(0, 0), (0, 0)],
    },
    {
        "matrix": [[1, -2, 3], [4, -5, 6], [7, -8, 9]],
        "expected_result": 18,
        "subarray_indices": [(0, 2), (2, 2)],
    },
    {
        "matrix": [[1, 2], [3, 4]],
        "expected_result": 10,
        "subarray_indices": [(0, 0), (1, 1)],
    },
    {
        "matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
        "expected_result": 78,
        "subarray_indices": [(0, 0), (3, 2)],
    },
    {
        "matrix": [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9], [-10, -11, -12]],
        "expected_result": -1,
        "subarray_indices": [(0, 0), (0, 0)],
    },
    {
        "matrix": [[1, -2, 3],
                   [4, -5, 6],
                   [7, -8, 9]],
        "expected_result": 18,
        "subarray_indices": [(0, 2), (2, 2)],
    },
    {
        "matrix": [[1, 2], [3, 4]],
        "expected_result": 10,
        "subarray_indices": [(0, 0), (1, 1)],
    },
    {
        "matrix": [
            [2, -1, 4, -6, 2],
            [-3, 2, -1, 4, -3],
            [1, -5, 2, -1, 5],
            [4, -2, 3, 7, -2],
        ],
        "expected_result": 14,
        "subarray_indices": [(0, 2), (3, 4)],
    },
    {
        "matrix": [
            [-2, 5, -1, 4],
            [8, -6, 3, 1],
            [2, 2, -4, -1],
            [-3, 2, 6, -1]],
        "expected_result": 15,
        "subarray_indices": [(0, 0), (3, 3)],
    },
    {
        "matrix": [[1, 1],
                   [1, 1], [1, 1], [1, 1]],
        "expected_result": 8,
        "subarray_indices": [(0, 0), (3, 1)],
    },
]

def print_subset(matrix, start_row, end_row, start_col, end_col):
  print("Printing the subset of the matrix :")
  for i in range(start_row, end_row+1):
      for j in range(start_col, end_col+1):
          print(matrix[i][j], end=" ")
      print()

def maxMatrixSum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Calculate cumulative sums
    cumulative_sums = [[0] * (cols + 1) for _ in range(rows + 1)]
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            cumulative_sums[i][j] = (
                matrix[i - 1][j - 1]
                + cumulative_sums[i - 1][j]
                + cumulative_sums[i][j - 1]
                - cumulative_sums[i - 1][j - 1]
            )

    max_sum = float('-inf')
    top, left, bottom, right = 0, 0, 0, 0

    # Calculate submatrix sums using cumulative sums
    for i1 in range(1, rows + 1):
        for j1 in range(1, cols + 1):
            for i2 in range(i1, rows + 1):
                for j2 in range(j1, cols + 1):
                    submatrix_sum = (
                        cumulative_sums[i2][j2]
                        - cumulative_sums[i1 - 1][j2]
                        - cumulative_sums[i2][j1 - 1]
                        + cumulative_sums[i1 - 1][j1 - 1]
                    )

                    if submatrix_sum > max_sum:
                        max_sum = submatrix_sum
                        top = i1 - 1
                        left = j1 - 1
                        bottom = i2 - 1
                        right = j2 - 1
    print("Maximum Subarray Sum:", max_sum)
    print_subset(matrix,top,bottom,left, right)
    print("Indices of Maximum Subarray:")
    print(f"Top: {top}, Left: {left}, Bottom: {bottom}, Right: {right}\n")

for i in range(len(tests)):
  matrix = tests[i]
  maxMatrixSum(matrix["matrix"])

count = []
# function to benchmark
def task():

    for i in range(len(tests)):
      matrix = tests[i]
      maxMatrixSum(matrix["matrix"])

if __name__ == '__main__':
    # run 3 times and record the durations
    times = list()
    for i in range(10):
        count.append(i+1)
        # record start time
        time_start = perf_counter()
        # run the task
        task()
        # calculate the duration
        time_duration = perf_counter() - time_start
        # report the duration
        print(f'>took {time_duration:.3f} seconds')
        # store the duration
        times.append(time_duration)
    # report the average duration
    time_average = sum(times) / 10.0
    print(f'Average time {time_average:.3f} seconds')

plt.plot(count,times,label="Time taken vs Count")
plt.axhline(y = time_average, color = 'r', linestyle = '--',label="Avg time taken")
plt.xlabel("Count")
plt.ylabel("Time taken in sec")
plt.title('Time taken each time')
plt.legend(bbox_to_anchor = (1.0, 1), loc = 'upper center')
plt.show()