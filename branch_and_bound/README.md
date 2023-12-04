# Advanced-Algorithm-Project-2023-2024
This repository is dedicated to solving the Matrix Maximum Segment Problem in a 2-dimensional scenario, commonly known as the Maximum Subarray Problem. Our primary objective is to implement various algorithms for this task and provide a comprehensive experimental analysis of their runtime performance and the quality of results. Explore this repository to access the code, documentation, and data related to our research and implementations.

Introduction:
This section implements algorithms for the maximum sub matrix problem using the branch and bound approach. The approach is implemented with two different implementatiions. All the algorithms outputs the maximum sum and tuple containg the indices of the submatix with maximum sum.

For the noth the implementations have the same inputs and outputs.

Non Constrained :

    max_sum, (i1, j1), (i1, j2) = max_segment_branch_and_bound(matrix)

Input : matrix - A 2D array or nested list
Output : maximum sum, indices of the first element of the submatrix as a tuple, indices of the last element of the submatrix as a tuple.

Constrained :

    max_sum, (i1, j1), (i1, j2) = max_segment_branch_and_bound_constrained(matrix, k, l)

Input : matrix - A 2D array or nested list, the constrains on the rows and columns, k and l respectively.
Output : maximum sum, indices of the first element of the submatrix as a tuple, indices of the last element of the submatrix as a tuple.

The constrained version is done only for the second implementation and not the first.

