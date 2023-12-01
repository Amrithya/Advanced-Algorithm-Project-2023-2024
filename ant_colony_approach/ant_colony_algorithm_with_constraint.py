import random
import numpy as np

random.seed(42)  # Set a random seed for reproducibility

class Ant:
    def __init__(self, position):
        self.position = position
        self.subarray_sum = 0

    def move(self, matrix, K, L):
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
        direction = random.choice(directions)
        new_x = min(max(self.position[0] + direction[0], 0), rows - K)
        new_y = min(max(self.position[1] + direction[1], 0), cols - L)
        self.position = (new_x, new_y)

    def calculate_subarray_sum(self, matrix, K, L):
        top, left = self.position
        self.subarray_sum = sum(matrix[i][j] for i in range(top, top + K) for j in range(left, left + L))

    def get_bottom_right(self, matrix, K, L):
        bottom = min(self.position[0] + K - 1, len(matrix) - 1)
        right = min(self.position[1] + L - 1, len(matrix[0]) - 1)
        return (bottom, right)

def initialize_ants(num_ants, matrix, K, L):
    ants = []
    for _ in range(num_ants):
        position = (random.randint(0, len(matrix) - K), random.randint(0, len(matrix[0]) - L))
        ants.append(Ant(position))
    return ants

def initialize_pheromone_matrix(matrix):
    return [[1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

def update_pheromones(ants, pheromone_matrix, evaporation_rate):
    for row in pheromone_matrix:
        for i in range(len(row)):
            row[i] *= (1 - evaporation_rate)

    for ant in ants:
        x, y = ant.position
        pheromone_matrix[x][y] += ant.subarray_sum  # Basic pheromone update

def find_best_solution(ants, matrix, K, L):
    best_ant = max(ants, key=lambda ant: ant.subarray_sum)
    return best_ant.subarray_sum, best_ant.position, best_ant.get_bottom_right(matrix, K, L)

def ant_colony_optimization(matrix, K, L, num_ants, num_iterations, evaporation_rate):
    if K > len(matrix) or L > len(matrix[0]):
        return -float('inf'), (0, 0), (0, 0)

    pheromone_matrix = initialize_pheromone_matrix(matrix)
    ants = initialize_ants(num_ants, matrix, K, L)

    for _ in range(num_iterations):
        for ant in ants:
            ant.move(matrix, K, L)
            ant.calculate_subarray_sum(matrix, K, L)

        update_pheromones(ants, pheromone_matrix, evaporation_rate)

    return find_best_solution(ants, matrix, K, L)


