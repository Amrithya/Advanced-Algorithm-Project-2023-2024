import random
random.seed(42)  # Set a random seed for reproducibility

class Ant:
    # Ant class constructor with an initial position and a sum variable.
    def __init__(self, position):
        self.position = position  # Current position of the ant in the matrix.
        self.subarray_sum = 0     # Sum of the subarray the ant covers.

    # Function to move the ant within the matrix boundaries.
    def move(self, matrix, K, L):
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Possible movement directions: right, left, down, up.
        direction = random.choice(directions)  # Randomly choose a direction.
        # Calculate new position ensuring the ant stays within the matrix bounds.
        new_x = min(max(self.position[0] + direction[0], 0), rows - K)
        new_y = min(max(self.position[1] + direction[1], 0), cols - L)
        self.position = (new_x, new_y)  # Update the ant's position.

    # Function to calculate the sum of the subarray at the ant's position.
    def calculate_subarray_sum(self, matrix, K, L):
        top, left = self.position
        # Calculate the sum of elements in the subarray defined by KxL size at the ant's position.
        self.subarray_sum = sum(matrix[i][j] for i in range(top, top + K) for j in range(left, left + L))

# Function to initialize a list of ants at random positions.
def initialize_ants(num_ants, matrix, K, L):
    ants = []
    for _ in range(num_ants):
        # Random initial position within matrix boundaries.
        position = (random.randint(0, len(matrix) - K), random.randint(0, len(matrix[0]) - L))
        ants.append(Ant(position))  # Create a new Ant instance and add it to the list.
    return ants

# Function to find the best solution among all ants.
def find_best_solution(ants, K, L):
    # Find the ant with the highest subarray sum.
    best_ant = max(ants, key=lambda ant: ant.subarray_sum)
    top_left = best_ant.position  # Top-left corner of the best subarray.
    # Calculate bottom-right corner of the best subarray.
    bottom_right = (best_ant.position[0] + K - 1, best_ant.position[1] + L - 1)
    return best_ant.subarray_sum, top_left, bottom_right

# Main function for ant colony optimization.
def ant_colony_optimization(matrix, K, L, num_ants=300, num_iterations=500):
    # Check for invalid inputs.
    if not matrix or K > len(matrix) or L > len(matrix[0]):
        return -float('inf'), (0, 0), (0, 0)

    # Initialize ants with random positions.
    ants = initialize_ants(num_ants, matrix, K, L)

    # Iterate through the number of iterations.
    for _ in range(num_iterations):
        for ant in ants:
            ant.move(matrix, K, L)  # Move each ant.
            ant.calculate_subarray_sum(matrix, K, L)  # Calculate the sum of the subarray at the new position.

    # Find the best solution among all ants.
    max_sum, top_left, bottom_right = find_best_solution(ants, K, L)
    return max_sum, top_left, bottom_right
