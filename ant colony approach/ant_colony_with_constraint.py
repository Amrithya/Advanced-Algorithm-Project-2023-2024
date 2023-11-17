import random
random.seed(42)  # Set a random seed for reproducibility

class Ant:
    # Time Complexity: O(num_iterations * num_ants * K * L + num_iterations * N * M)
    # Space Complexity: O(N * M + num_ants)
    def __init__(self, position):
        """
        Initialize an ant at a given position.
        :param position: Tuple representing the top-left corner of the subarray.
        """
        self.position = position
        self.subarray_sum = 0

    def move(self, matrix, K, L):
        """
        Move the ant to a new position within the matrix boundaries.
        :param matrix: 2D list of integers.
        :param K: Number of rows in the subarray.
        :param L: Number of columns in the subarray.
        """
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
        direction = random.choice(directions)
        new_x = min(max(self.position[0] + direction[0], 0), rows - K)
        new_y = min(max(self.position[1] + direction[1], 0), cols - L)
        self.position = (new_x, new_y)

    def calculate_subarray_sum(self, matrix, K, L):
        """
        Calculate the sum of the subarray at the ant's current position.
        :param matrix: 2D list of integers.
        :param K: Number of rows in the subarray.
        :param L: Number of columns in the subarray.
        """
        top, left = self.position
        self.subarray_sum = sum(matrix[i][j] for i in range(top, top + K) for j in range(left, left + L))

    def get_bottom_right(self, K, L):
        """
        Calculate the bottom right index of the current subarray.
        :param K: Number of rows in the subarray.
        :param L: Number of columns in the subarray.
        :return: Tuple representing the bottom-right corner of the subarray.
        """
        bottom = min(self.position[0] + K - 1, len(matrix) - 1)
        right = min(self.position[1] + L - 1, len(matrix[0]) - 1)
        return (bottom, right)

def initialize_ants(num_ants, matrix, K, L):
    """
    Initialize a specified number of ants randomly placed on the matrix.
    :param num_ants: Number of ants to initialize.
    :param matrix: 2D list of integers.
    :param K: Number of rows in the subarray.
    :param L: Number of columns in the subarray.
    :return: List of Ant objects.
    """
    ants = []
    for _ in range(num_ants):
        position = (random.randint(0, len(matrix) - K), random.randint(0, len(matrix[0]) - L))
        ants.append(Ant(position))
    return ants

def initialize_pheromone_matrix(matrix):
    """
    Initialize the pheromone matrix with equal pheromone levels for all cells.
    :param matrix: 2D list of integers.
    :return: 2D list representing the pheromone levels.
    """
    return [[1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

def update_pheromones(ants, pheromone_matrix, evaporation_rate):
    """
    Update the pheromone levels on the matrix based on ants' subarray sums.
    :param ants: List of Ant objects.
    :param pheromone_matrix: 2D list representing the pheromone levels.
    :param evaporation_rate: Rate at which pheromones evaporate.
    """
    for row in pheromone_matrix:
        for i in range(len(row)):
            row[i] *= (1 - evaporation_rate)

    for ant in ants:
        x, y = ant.position
        pheromone_matrix[x][y] += ant.subarray_sum  # Basic pheromone update

def find_best_solution(ants, K, L):
    """
    Find the best solution (subarray with maximum sum) from all ants.
    :param ants: List of Ant objects.
    :param K: Number of rows in the subarray.
    :param L: Number of columns in the subarray.
    :return: Tuple of maximum subarray sum, top-left and bottom-right indices.
    """
    best_ant = max(ants, key=lambda ant: ant.subarray_sum)
    return best_ant.subarray_sum, best_ant.position, best_ant.get_bottom_right(K, L)

def ant_colony_optimization(matrix, K, L, num_ants, num_iterations, evaporation_rate):
    """
    Ant Colony Optimization algorithm for 2D Maximum Subarray Problem.
    :param matrix: 2D list of integers.
    :param K: Number of rows in the subarray.
    :param L: Number of columns in the subarray.
    :param num_ants: Number of ants.
    :param num_iterations: Number of iterations to run the algorithm.
    :param evaporation_rate: Rate at which pheromones evaporate.
    :return: Tuple of maximum subarray sum, top-left and bottom-right indices.
    """
    pheromone_matrix = initialize_pheromone_matrix(matrix)
    ants = initialize_ants(num_ants, matrix, K, L)

    for _ in range(num_iterations):
        for ant in ants:
            ant.move(matrix, K, L)
            ant.calculate_subarray_sum(matrix, K, L)

        update_pheromones(ants, pheromone_matrix, evaporation_rate)

    return find_best_solution(ants, K, L)

# Usage example
matrix = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]
K, L = 1, 1
num_ants = 10
num_iterations = 100
evaporation_rate = 0.5

result, top_left, bottom_right = ant_colony_optimization(matrix, K, L, num_ants, num_iterations, evaporation_rate)
print("Maximum Subarray Sum:", result)
print("Top Left Index of Subarray:", top_left)
print("Bottom Right Index of Subarray:", bottom_right)
