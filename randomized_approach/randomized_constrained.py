import random

def random_fixed_size_submatrix_sum(matrix, K, L):
    M, N = len(matrix), len(matrix[0])
    num_iterations= int((M*(M+1)*N*(N*1))/4)
    max_sum = float('-inf')
    best_submatrix = None

    for _ in range(num_iterations):
        i1 = random.randint(0, M - K)
        j1 = random.randint(0, N - L)
        i2 = i1 + K - 1
        j2 = j1 + L - 1

        current_sum = sum(matrix[i][j] for i in range(i1, i2 + 1) for j in range(j1, j2 + 1))

        if current_sum > max_sum:
            max_sum = current_sum
            best_submatrix = ((i1, j1), (i2, j2))

    return max_sum, best_submatrix[0], best_submatrix[1]
