import numpy as np
import random
import time
import matplotlib.pyplot as plt

# Genetic Algorithms
def max_segment_2d_genetic(matrix, population_size=100, num_generations=100):
    """
    Maximizes the sum of a submatrix in a 2D array using a genetic algorithm.
   
    Parameters:
    - matrix (numpy.ndarray): The input 2D array.
    - population_size (int): The size of the population in each generation.
    - num_generations (int): The number of generations for the genetic algorithm.

    Returns:
    - tuple: The indices (i1, i2, j1, j2) representing the submatrix with the maximum sum.
    """
    # Time Complexity: O(population_size * num_generations * fitness_function_time)
    # Space Complexity: O(population_size * solution_size)
    # Quality: The quality of the result depends on the effectiveness of the genetic operators (crossover and mutation).
    # Running Time: Depends on population_size and num_generations; can be fast for small populations and generations.

    # Function to generate a random program (candidate solution) respecting the constraints
    def generate_program(matrix):
        """
        Generates a random program (submatrix indices) respecting the constraints.

        Parameters:
        - matrix (numpy.ndarray): The input 2D array.
        - rows (int): The number of rows in the matrix.
        - cols (int): The number of columns in the matrix.

        Returns:
        - tuple: The indices (i1, i2, j1, j2) representing the generated program.
        """
        rows, cols = matrix.shape
        i1 = random.randint(0, rows - 1)
        i2 = random.randint(i1, rows - 1)
        j1 = random.randint(0, cols - 1)
        j2 = random.randint(j1, cols - 1)
        return i1, i2, j1, j2

    # Function to evaluate the fitness of a program respecting the constraints
    def fitness(program, matrix):
        """
        Evaluates the fitness (sum of submatrix) of a program respecting the constraints.

        Parameters:
        - program (tuple): The indices (i1, i2, j1, j2) of the program.
        - matrix (numpy.ndarray): The input 2D array.

        Returns:
        - int: The fitness value (sum of elements in the submatrix).
        """
        i1, i2, j1, j2 = program
        submatrix = matrix[i1:i2 + 1, j1:j2 + 1]
        return np.sum(submatrix)

    # Function to recombine two programs respecting the constraints
    def recombine(program1, program2):
        """
        Recombines two programs respecting the constraints.

        Parameters:
        - program1 (tuple): The indices (i1, i2, j1, j2) of the first program.
        - program2 (tuple): The indices (i1, i2, j1, j2) of the second program.

        Returns:
        - tuple: The indices (i1, i2, j1, j2) representing the recombined program.
        """
        
        i1 = max(program1[0], program2[0])
        i2 = min(program1[1], program2[1])
        j1 = max(program1[2], program2[2])
        j2 = min(program1[3], program2[3])
        
        # Ensure valid submatrix, otherwise fallback to generating a new program
        if i1 <= i2 and j1 <= j2:
            return i1, i2, j1, j2
        else:
            return generate_program(matrix)

    # Function to mutate a program respecting the constraints
    def mutate(program, rows, cols):
        """
        Mutates a program respecting the constraints.

        Parameters:
        - program (tuple): The indices (i1, i2, j1, j2) of the program.
        - rows (int): The number of rows in the matrix.
        - cols (int): The number of columns in the matrix.
        - mutation_probability (float): Probability of mutation for each gene.

        Returns:
        - tuple: The indices (i1, i2, j1, j2) representing the mutated program.
        """
        i1, i2, j1, j2 = program
        if random.random() < 0.2:
            i1 = random.randint(0, i2)
        if random.random() < 0.2:
            i2 = random.randint(i1, rows - 1)
        if random.random() < 0.2:
            j1 = random.randint(0, j2)
        if random.random() < 0.2:
            j2 = random.randint(j1, cols - 1)
        return i1, i2, j1, j2

    # Initialization of the population with random programs respecting the constraints
    population = [generate_program(matrix) for _ in range(population_size)]

    # Main loop for genetic algorithm
    for generation in range(num_generations):
        population = sorted(population, key=lambda program: -fitness(program, matrix))

        selected_programs = population[:population_size // 2]

        new_population = selected_programs.copy()
        while len(new_population) < population_size:
            parent1, parent2 = random.choices(selected_programs, k=2)
            child = recombine(parent1, parent2)
            child = mutate(child, matrix.shape[0], matrix.shape[1])  # Pass rows and cols to mutate
            new_population.append(child)

        population = new_population

    # Return the program with the maximum fitness (maximum sum of submatrix)
    return max(population, key=lambda program: fitness(program, matrix))

# Function to generate an initial solution (random submatrix)
def generate_solution(matrix):
    """
    Generates a random initial solution (submatrix) respecting the array dimensions.

    Parameters:
    - matrix (numpy.ndarray): The input 2D array.

    Returns:
    - tuple: The indices (i1, i2, j1, j2) representing the initial submatrix.
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
    Evaluates the sum of elements in a submatrix.

    Parameters:
    - solution (tuple): The indices (i1, i2, j1, j2) representing the submatrix.
    - matrix (numpy.ndarray): The input 2D array.

    Returns:
    - int: The sum of elements in the submatrix.
    """
    i1, i2, j1, j2 = solution
    submatrix = matrix[i1:i2 + 1, j1:j2 + 1]
    return np.sum(submatrix)