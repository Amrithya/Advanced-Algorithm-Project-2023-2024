def max_sum_rectangle(matrix):
    rows, cols = len(matrix), len(matrix[0])

    # Compute 2D prefix sum
    prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            prefix_sum[i][j] = matrix[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

    max_sum = float('-inf')
    top, left, bottom, right = 0, 0, 0, 0

    for row_start in range(1, rows + 1):
        for row_end in range(row_start, rows + 1):
            for col_start in range(1, cols + 1):
                for col_end in range(col_start, cols + 1):
                    current_sum = prefix_sum[row_end][col_end] - prefix_sum[row_end][col_start - 1] - prefix_sum[row_start - 1][col_end] + prefix_sum[row_start - 1][col_start - 1]

                    if current_sum > max_sum:
                        max_sum = current_sum
                        top, left, bottom, right = row_start - 1, col_start - 1, row_end - 1, col_end - 1

    return max_sum, (top, left), (bottom, right)

# Example usage:
matrix = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

result, top_left, bottom_right = max_sum_rectangle(matrix)
print("Maximum Sum of Contiguous Elements:", result)
print("Top-left Index:", top_left)
print("Bottom-right Index:", bottom_right)
