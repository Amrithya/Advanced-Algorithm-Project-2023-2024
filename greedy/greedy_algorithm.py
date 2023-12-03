"""helper function which is kadane's greedy algorithm for getting the maxmimum sub array in 1D"""
def max_subarray_sum_1d_with_indices(arr): # kadane algorithm 
    max_sum = float('-inf')
    current_sum = 0
    current_start = temp_start = temp_end = 0

    for i, num in enumerate(arr):
        if current_sum + num < num:
            current_sum = num
            current_start = i
        else:
            current_sum += num

        if current_sum > max_sum:
            max_sum = current_sum
            temp_start = current_start
            temp_end = i

    return max_sum, temp_start, temp_end


# Non constrained Greedy Algorithm
def greedy_algorithm_non_constrained(matrix):
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












