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

# Modify your main function to include ACO
def main():
      # Define the list of test cases
    tests = [
        {
            "matrix": [
                [1, 2, -1, -4, -20],
                [-8, -3, 4, 2, 1],
                [3, 8, 10, 1, 3],
                [-4, -1, 1, 7, -6],
            ],
        },
        {
            "matrix": [
                [1, 2, -1, -4, -20],
                [-8, -3, 4, 2, 1],
                [3, 8, 10, 1, 3],
                [-4, -1, 1, 7, -6],
            ],
        },
        {
            "matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        },
        {
            "matrix": [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]],
        },
        {
            "matrix": [[1, -2, 3], [4, -5, 6], [7, -8, 9]],
        },
        {
            "matrix": [[1, 2], [3, 4]],
        },
        {
            "matrix": [
                [2, -1, 4, -6, 2],
                [-3, 2, -1, 4, -3],
                [1, -5, 2, -1, 5],
                [4, -2, 3, 7, -2],
            ],
        },
        {
            "matrix": [[-2, 5, -1, 4], [8, -6, 3, 1], [2, 2, -4, -1], [-3, 2, 6, -1]],
        },
        {
            "matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
        },
        {
            "matrix": [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9], [-10, -11, -12]],
        },
        {
            "matrix": [[1, -2, 3], [4, -5, 6], [7, -8, 9]],
        },
        {
            "matrix": [[1, 2], [3, 4]],
        },
        {
            "matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
        },
        {
            "matrix": [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9], [-10, -11, -12]],
        },
        {
            "matrix": [[1, -2, 3], [4, -5, 6], [7, -8, 9]],
        },
        {
            "matrix": [[1, 2], [3, 4]],
        },
        {
            "matrix": [
                [2, -1, 4, -6, 2],
                [-3, 2, -1, 4, -3],
                [1, -5, 2, -1, 5],
                [4, -2, 3, 7, -2],
            ],
        },
        {
            "matrix": [[-2, 5, -1, 4], [8, -6, 3, 1], [2, 2, -4, -1], [-3, 2, 6, -1]],
        },
        {
            "matrix": [[1, 1], [1, 1], [1, 1], [1, 1]],
        },
    ]
    # Additional Test Case
    large_matrix_test = {
    "matrix": np.random.randint(-100, 100, size=(1000, 1000)),}
    # Add the new test case to the list of tests
    tests.append(large_matrix_test)
    # Iterate through the test cases
    for test in tests:
        matrix = np.array(test["matrix"])

        # Apply the genetic algorithm
        # ... (your existing code)

        # Apply the Ant Colony Optimization
        # Apply the Ant Colony Optimization
        start_time_aco = time.time()
        i1_aco, i2_aco, j1_aco, j2_aco = ant_colony_algorithm(matrix)
        end_time_aco = time.time()

        max_sum_aco = matrix[i1_aco:i2_aco + 1, j1_aco:j2_aco + 1].sum()
        execution_time_aco = end_time_aco - start_time_aco

        # Print the results for ACO
        print("Ant Colony Optimization:")
        print(f"Matrix:")
        print(matrix)
        print(f"Maximum Segment Sum: {max_sum_aco}")
        print(f"Indices (i1, i2, j1, j2): ({i1_aco}, {i2_aco}, {j1_aco}, {j2_aco}")
        print(f"Execution Time: {execution_time_aco} seconds")
        print("=" * 30)

        # Plot the matrix for ACO
        plt.xlabel('Algorithms')
        plt.ylabel('Maximum Segment Sum')
        plt.imshow(matrix, cmap='viridis')
        plt.title(f'Original Matrix\nMaximum Segment Sum: {max_sum_aco}')
        plt.colorbar()
        plt.show()

        # Plot the selected submatrix for ACO
        plt.imshow(matrix[i1_aco:i2_aco + 1, j1_aco:j2_aco + 1], cmap='viridis')
        plt.title('Selected Submatrix (ACO)')
        plt.colorbar()
        # Annotate the plot with Maximum Segment Sum
        plt.annotate(f'Max Sum: {max_sum_aco}', xy=(0.5, 0.5), xytext=(30, 10),
                     textcoords='offset points', color='white', fontsize=12, bbox=dict(facecolor='black', alpha=0.7))
        plt.show()

# Call the main function
if __name__ == "__main__":
    main()