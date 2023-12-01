import numpy as np  # Importing the numpy library as 'np' for efficient numerical operations.
import random  # Importing the 'random' module to generate random numbers.
import time  # Importing the 'time' module to measure execution time.
import matplotlib.pyplot as plt  # Importing the 'matplotlib.pyplot' module for data visualization.


# Ant Colony Optimization
def ant_colony_algorithm(matrix, num_ants=10, num_iterations=100):
    """
    Ant Colony Optimization algorithm to find the maximum segment sum in a 2D matrix.

    Parameters:
    - matrix (numpy.ndarray): The 2D matrix for which the maximum segment sum is to be found.
    - num_ants (int): The number of ants used in the algorithm.
    - num_iterations (int): The number of iterations to perform.

    Returns:
    - tuple: A tuple representing the best solution found, i.e., (i1, i2, j1, j2).
    """
    # Time Complexity: O(num_ants * num_iterations * solution_evaluation_time)
    # Space Complexity: O(1) (constant space for storing best_solution and best_score)
    # Quality: The quality of the result heavily depends on the randomness of ant movements. May not always find the global optimum.
    # Running Time: Depends on the value of num_ants and num_iterations; typically slower than genetic algorithms.

    best_solution = generate_solution(matrix)
    best_score = evaluate_solution(best_solution, matrix)

    for _ in range(num_iterations):
        for _ in range(num_ants):
            new_solution = generate_solution(matrix)
            new_score = evaluate_solution(new_solution, matrix)

            if new_score > best_score:
                best_solution = new_solution
                best_score = new_score

    return best_solution

# Function to generate an initial solution (random submatrix)
def generate_solution(matrix):
    """
    Generate a random solution (submatrix indices) for the given matrix.

    Parameters:
    - matrix (numpy.ndarray): The 2D matrix.

    Returns:
    - tuple: A tuple representing the random solution (i1, i2, j1, j2).
    """
    rows, cols = matrix.shape
    i1 = random.randint(0, rows - 1)
    i2 = random.randint(i1, rows - 1)
    j1 = random.randint(0, cols - 1)
    j2 = random.randint(j1, cols - 1)
    return i1, i2, j1, j2

# Function to evaluate a solution (sum of elements in the submatrix)
def evaluate_solution(solution, matrix):
    """
    Evaluate the sum of elements in the submatrix defined by the given solution.

    Parameters:
    - solution (tuple): A tuple representing the solution (i1, i2, j1, j2).
    - matrix (numpy.ndarray): The 2D matrix.

    Returns:
    - int: The sum of elements in the submatrix.
    """
    i1, i2, j1, j2 = solution
    submatrix = matrix[i1:i2 + 1, j1:j2 + 1]
    return np.sum(submatrix)
