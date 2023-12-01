import random
r = 1000

def initialize_submatrices(matrix):
    rows, cols = len(matrix), len(matrix[0])
    submatrices = []

    for top in range(rows):
        for bottom in range(top, rows):
            for left in range(cols):
                for right in range(left, cols):
                    submatrices.append(((top, left), (bottom, right)))

    return submatrices

def random_submatrix_sum(matrix):
    submatrices = initialize_submatrices(matrix)
    max_sum = float('-inf')
    best_submatrix = None

    for _ in range(r):   
        random_submatrix = random.choice(submatrices)
        top, left = random_submatrix[0]
        bottom, right = random_submatrix[1]

        current_sum = sum(matrix[i][j] for i in range(top, bottom + 1) for j in range(left, right + 1))

        if current_sum > max_sum:
            max_sum = current_sum
            best_submatrix = random_submatrix

    return max_sum, best_submatrix

matrix = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

result, best_submatrix = random_submatrix_sum(matrix)
print("Maximum Sum of Contiguous Elements:", result)
print("Best Submatrix:", best_submatrix)