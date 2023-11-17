# Advanced-Algorithm-Project-2023-2024
This repository is dedicated to solving the Matrix Maximum Segment Problem in a 2-dimensional scenario, commonly known as the Maximum Subarray Problem. Our primary objective is to implement various algorithms for this task and provide a comprehensive experimental analysis of their runtime performance and the quality of results. Explore this repository to access the code, documentation, and data related to our research and implementations.


Algorithm:

Input: matrix A

Output: values i1, i2, j1, j2 such that the submatrix A[i1 to i2, j1 to j2] have the maximum sum
    
1. intialize sum to -infinity
2. Take matrix A to be the root node and calculate the sum of all elements of A.
3. if sum <sum(A):

    sum = sum(A)

5. add A to a queue
6. while the queue is non empty:

        retrieve the last element of the queue and delete it from the queue
        generate all possible sub arrays of that element
        for subarray in all sub arrays of the element:
            if sum(subarray)>sum:
                sum = sum(subarray)
                add subarray to the queue
            
7. return(sum, indices of the max sub array)
