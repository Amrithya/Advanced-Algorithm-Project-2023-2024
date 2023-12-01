# Advanced-Algorithm-Project-2023-2024
This repository is dedicated to solving the Matrix Maximum Segment Problem in a 2-dimensional scenario, commonly known as the Maximum Subarray Problem. Our primary objective is to implement various algorithms for this task and provide a comprehensive experimental analysis of their runtime performance and the quality of results. Explore this repository to access the code, documentation, and data related to our research and implementations.


Algorithm:

Input: matrix A

Output: values i1, i2, j1, j2 such that the submatrix A[i1 to i2, j1 to j2] have the maximum sum
    
1. intialize indices to [0, number of rows, 0, number of columns] sum to sum of the whole matrix and positive_sum to be the sum of all positive elements of the matrix
2. add the indices of the matrix, sum of the elements and positive sum of the matrix 
3. while the queue is non empty:

        retrieve the last element of the queue and delete it from the queue
        generate all possible sub arrays of that element
        for subarray in all sub arrays of the element:
            if positive sum(subarray) > sum:
               add the subarray to the queue
               if sum(subarray) > sum:
                update sum to sum of sum(subrray) and the indices to the indices of the subarray.
            
7. return(sum, indices of the max sub array)
