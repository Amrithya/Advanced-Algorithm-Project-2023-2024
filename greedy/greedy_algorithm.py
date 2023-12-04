
def max_subarray_sum_1d_with_indices(arr): # kadane algorithm 
    """
    This function implements Kadane's algorithm to find the maximum subarray sum in a 1D array. 
    The function works by initializing a current sum and a maximum sum. 
    As it iterates over the array, it compares the current sum with the next element and makes a greedy choice of  
    whether to start a new subarray or to continue with the current one. 
    It updates the maximum sum and its corresponding indices when a new maximum is found.

    Args:
    arr (list): A 1D array (list) of numbers. The elements of the array can be any integer values, 
                both positive and negative.

    Returns:
    tuple: A tuple containing three elements:
           - The first element is the maximum subarray sum (int).
           - The second element is the start index (int) of the subarray with this maximum sum.
           - The third element is the end index (int) of the subarray with this maximum sum.
    """
    
    max_sum = float('-inf')  # Initialize the maximum sum to negative infinity to handle all possible cases, including negative numbers
    current_sum = 0  # Initialize the current sum for the ongoing subarray
    current_start = temp_start = temp_end = 0  # Initialize start and end indices for the maximum and temporary subarrays
    
    
    # Iterate through each number in the array, with its index
    for i, num in enumerate(arr):  
        
        # Start a new subarray if it leads to a larger sum and update start index
        if current_sum + num < num:
            current_sum = num  
            current_start = i  
            
        # Continue the current subarray by adding the current number    
        else: 
            current_sum += num  

        # if a new max_sum is found update the max_sum, start index and end index
        if current_sum > max_sum:
            max_sum = current_sum  
            temp_start = current_start  
            temp_end = i  

    return max_sum, temp_start, temp_end  



# Non constrained Greedy Algorithm
def greedy_algorithm_non_constrained(matrix):
    """
    This function uses a greedy approach to find the maximum subarray sum in a 2D array (matrix) without constraints by transforming
    it into a 1D problem.
    
    Outer Loop fixes a left column. 
    For each left column, it initializes a temporary array temp with a length equal to the number of rows.
    This array will store the running sum of elements in the rows between the left and right column pointers.
    
    For each right column in the inner loop, the function updates the temp array with the sum of elements in each row from the left
    column to the current right column. The function applys a greedy version of kadane's finds the maximum sum contiguous subarray 
    in a 1D array, which in this case is used to find the rows that contribute to the maximum sum between the left and right 
    column boundaries. 
    
    If the sum found by Kadane's algorithm for the current left-right column pair is greater than the current max_sum, the function
    updates max_sum and the coordinates of the top-left and bottom-right corners of the submatrix.
    Args:
    matrix (list of lists): A 2D array (list of lists) of numbers. The elements of the matrix can be any integer values,
    both positive and negative.
    
    Args:
    matrix : A 2D array (list) of numbers. 

    Returns:
    tuple: A tuple containing:
           - The first element is the maximum subarray sum (int).
           - The second element is a tuple of the start row and column indices (int, int) of the subarray.
           - The third element is a tuple of the end row and column indices (int, int) of the subarray.
    """
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    max_sum = float('-inf')
    start_row = end_row = start_col = end_col = -1

    # fix a left column
    for left in range(cols):
        temp = [0] * rows
        # lopp over all the columns from left to right
        for right in range(left, cols):
            # calculate running sum of rows until the right column and store it in a 1D Array  temp 
            for i in range(rows):
                temp[i] += matrix[i][right]
            # run kadane's algorithm to calculate the best sum subarray in 1D
            current_sum, current_start_row, current_end_row = max_subarray_sum_1d_with_indices(temp)
            if current_sum > max_sum:
                max_sum = current_sum   
                start_row, end_row, start_col, end_col = current_start_row, current_end_row, left, right
    
    return max_sum, (start_row, start_col), (end_row, end_col)












