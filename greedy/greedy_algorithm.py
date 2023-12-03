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



def modified_kadanes_with_constraints(arr, k):
    max_sum = float('-inf')
    current_sum = 0
    start = end = 0
    queue = []

    for i, num in enumerate(arr):
        current_sum += num
        queue.append(num)

        if i >= k:
            current_sum -= queue.pop(0)
            start += 1

        if current_sum > max_sum:
            max_sum = current_sum
            end = i

    return max_sum, start, end


def greedy_algorithm_constrained(matrix, k, l):
    rows, cols = len(matrix), len(matrix[0])
    if k > rows or l > cols:
        return "Constraints exceed matrix dimensions"

    max_sum = float('-inf')
    final_top = final_left = final_bottom = final_right = 0

    for left in range(cols):
        temp = [0] * rows

        for right in range(left, min(left + l, cols)):
            for i in range(rows):
                temp[i] += matrix[i][right]

            if right - left + 1 == l:
                current_max, top, bottom = modified_kadanes_with_constraints(temp, k)
                if current_max > max_sum:
                    max_sum = current_max
                    final_top, final_bottom = top, bottom
                    final_left, final_right = left, right

    return max_sum, (final_top, final_left), (final_bottom, final_right)







