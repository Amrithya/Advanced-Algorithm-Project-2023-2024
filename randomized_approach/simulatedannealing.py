import random
import math

def random_submatrix(matrix):
    start_row = random.randint(0, len(matrix) - 1)
    end_row = random.randint(start_row, len(matrix) - 1)
    start_col = random.randint(0, len(matrix[0]) - 1)
    end_col = random.randint(start_col, len(matrix[0]) - 1)

    return start_row, start_col, end_row, end_col

def cost_function(matrix, submatrix):
    start_row, start_col, end_row, end_col = submatrix
    return sum(matrix[i][j] for i in range(start_row, end_row + 1) for j in range(start_col, end_col + 1))

def simulated_annealing(matrix, initial_temperature, cooling_rate, max_iterations):
    current_solution = random_submatrix(matrix)
    current_cost = cost_function(matrix, current_solution)

    best_solution = current_solution
    best_cost = current_cost

    temperature = initial_temperature

    for iteration in range(max_iterations):
        new_solution = random_submatrix(matrix)
        new_cost = cost_function(matrix, new_solution)

        if new_cost > current_cost or random.uniform(0, 1) < math.exp((new_cost - current_cost) / temperature):
            current_solution = new_solution
            current_cost = new_cost

        if current_cost > best_cost:
            best_solution = current_solution
            best_cost = current_cost

        temperature *= cooling_rate

    return best_solution, best_cost

matrix = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

initial_temperature = 1000
cooling_rate = 0.99
max_iterations = 1000

best_solution, best_cost = simulated_annealing(matrix, initial_temperature, cooling_rate, max_iterations)
start_row, start_col, end_row, end_col = best_solution

print("Top-left Index:", (start_row, start_col))
print("Bottom-right Index:", (end_row, end_col))
print("Best Cost:", best_cost)
