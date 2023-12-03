import numpy as np
import random

def calculate_iterations(M, N):
    c = 0.5 
    b = 100  
    iterations = int(c * (M + N) + b)
    return max(iterations, b) 

def calculate_trials(M, N):
    b = 100  
    trials = (M * N) + b
    return max(trials, b) 


def create_cumulative_sum_matrix(matrix):
    cum_sum_matrix = np.pad(matrix, ((1, 0), (1, 0)), mode='constant')
    cum_sum_matrix[1:, 1:] = np.cumsum(np.cumsum(matrix, axis=0), axis=1)
    return cum_sum_matrix

def submatrix_sum(cum_sum_matrix, top_left, bottom_right):
    tl_x, tl_y = top_left
    br_x, br_y = bottom_right
    return cum_sum_matrix[br_x + 1, br_y + 1] - cum_sum_matrix[tl_x, br_y + 1] - cum_sum_matrix[br_x + 1, tl_y] + cum_sum_matrix[tl_x, tl_y]

def gradient_descent_submatrix(cum_sum_matrix, M, N):
    max_iterations = calculate_iterations(M, N)
    max_sum = float('-inf')
    best_submatrix = ((0, 0), (0, 0))

    # Random initialization of submatrix
    top_left = (random.randint(0, M-1), random.randint(0, N-1))
    bottom_right = (random.randint(top_left[0], M-1), random.randint(top_left[1], N-1))

    for _ in range(max_iterations):
        current_sum = submatrix_sum(cum_sum_matrix, top_left, bottom_right)
        if current_sum > max_sum:
            max_sum = current_sum
            best_submatrix = (top_left, bottom_right)

        # Adjustments: expand, shrink, or move
        adjustments = {
            "expand_down": ((top_left[0], top_left[1]), (min(bottom_right[0] + 1, M-1), bottom_right[1])),
            "expand_right": ((top_left[0], top_left[1]), (bottom_right[0], min(bottom_right[1] + 1, N-1))),
            "shrink_up": ((min(top_left[0] + 1, bottom_right[0]), top_left[1]), bottom_right),
            "shrink_left": ((top_left[0], min(top_left[1] + 1, bottom_right[1])), bottom_right),
            "move_up": ((max(top_left[0] - 1, 0), top_left[1]), bottom_right),
            "move_down": ((min(top_left[0] + 1, M-1), top_left[1]), bottom_right),
            "move_left": ((top_left[0], max(top_left[1] - 1, 0)), bottom_right),
            "move_right": ((top_left[0], min(top_left[1] + 1, N-1)), bottom_right)
        }

        best_adjustment = None
        for adj, new_coords in adjustments.items():
            new_sum = submatrix_sum(cum_sum_matrix, new_coords[0], new_coords[1])
            if new_sum > current_sum:
                best_adjustment = new_coords
                current_sum = new_sum

        if best_adjustment:
            top_left, bottom_right = best_adjustment
        else:
            break  # No improvement found

    return max_sum, best_submatrix

def find_max_sum_submatrix(matrix):
    M, N = np.array(matrix).shape
    num_trials = calculate_trials(M, N)
    max_iterations_per_trial = calculate_iterations(M, N)
    cum_sum_matrix = create_cumulative_sum_matrix(matrix)
    overall_max_sum = float('-inf')
    overall_best_submatrix = ((0, 0), (0, 0))

    for _ in range(num_trials):
        max_sum, best_submatrix = gradient_descent_submatrix(cum_sum_matrix, M, N)
        if max_sum > overall_max_sum:
            overall_max_sum = max_sum
            overall_best_submatrix = best_submatrix

    return overall_max_sum, overall_best_submatrix[0], overall_best_submatrix[1]
