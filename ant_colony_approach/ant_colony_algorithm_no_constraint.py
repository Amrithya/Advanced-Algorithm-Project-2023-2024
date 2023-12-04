import random

def calculate_subarray_sum(matrix, i1, i2, j1, j2):
    sum = 0
    for i in range(i1, i2 + 1):
        for j in range(j1, j2 + 1):
            sum += matrix[i][j]
    return sum

def ant_colony_algorithm(matrix, num_ants=200, num_iterations=400, evaporation_rate=0.1):
    rows, cols = len(matrix), len(matrix[0]) if matrix else 0
    pheromone_matrix = initialize_pheromone_matrix(rows, cols)

    best_solution = None
    max_sum = float('-inf')

    for _ in range(num_iterations):
        solutions = []
        for _ in range(num_ants):
            solution = generate_random_solution(rows, cols)
            current_sum = calculate_subarray_sum(matrix, *solution)
            solutions.append((solution, current_sum))

            if current_sum > max_sum:
                best_solution, max_sum = solution, current_sum

        update_pheromone_matrix(pheromone_matrix, solutions, evaporation_rate)

    top_left = (best_solution[0], best_solution[2])
    bottom_right = (best_solution[1], best_solution[3])
    return max_sum, top_left, bottom_right

def initialize_pheromone_matrix(rows, cols):
    return [[1 for _ in range(cols)] for _ in range(rows)]

def generate_random_solution(rows, cols):
    i1, j1 = random.randint(0, rows-1), random.randint(0, cols-1)
    i2, j2 = random.randint(i1, rows-1), random.randint(j1, cols-1)
    return (i1, i2, j1, j2)

def update_pheromone_matrix(pheromone_matrix, solutions, evaporation_rate):
    for i in range(len(pheromone_matrix)):
        for j in range(len(pheromone_matrix[0])):
            pheromone_matrix[i][j] *= (1 - evaporation_rate)

    for solution, score in solutions:
        i1, i2, j1, j2 = solution
        for i in range(i1, i2 + 1):
            for j in range(j1, j2 + 1):
                pheromone_matrix[i][j] += score

