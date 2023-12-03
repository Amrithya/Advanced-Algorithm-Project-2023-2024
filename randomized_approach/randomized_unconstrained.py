import random

def preprocess_sum_matrix(matrix):
    M, N = len(matrix), len(matrix[0])
    sum_matrix = [[0] * (N + 1) for _ in range(M + 1)]

    for i in range(1, M + 1):
        for j in range(1, N + 1):
            sum_matrix[i][j] = (sum_matrix[i - 1][j] + sum_matrix[i][j - 1] -
                                sum_matrix[i - 1][j - 1] + matrix[i - 1][j - 1])

    return sum_matrix

def submatrix_sum(sum_matrix, top, left, bottom, right):
    return (sum_matrix[bottom + 1][right + 1] - sum_matrix[top][right + 1] -
            sum_matrix[bottom + 1][left] + sum_matrix[top][left])

def random_submatrix_sum(matrix):
    M, N = len(matrix), len(matrix[0])
    num_iterations= int((M*(M+1)*N*(N*1))/2)

    sum_matrix = preprocess_sum_matrix(matrix)
    submatrices = [((top, left), (bottom, right))
                   for top in range(M) for bottom in range(top, M)
                   for left in range(N) for right in range(left, N)]

    random.shuffle(submatrices)
    max_sum = float('-inf')
    best_submatrix = None

    for submatrix in submatrices[:num_iterations]:
        top, left = submatrix[0]
        bottom, right = submatrix[1]

        current_sum = submatrix_sum(sum_matrix, top, left, bottom, right)

        if current_sum > max_sum:
            max_sum = current_sum
            best_submatrix = submatrix

    return max_sum, best_submatrix[0], best_submatrix[1]
