import random
random.seed(42)  # Set a random seed for reproducibility

      
# Genetic Algorithm for Maximizing the Sum of a Submatrix in a 2D Array
def max_segment_2d_genetic(matrix, population_size=100, num_generations=100):
    """
    Maximizes the sum of a submatrix in a 2D array using a genetic algorithm.
   
    Parameters:
    - matrix (list): The input 2D array represented as a list of lists.
    - population_size (int): The size of the population in each generation.
    - num_generations (int): The number of generations for the genetic algorithm.

    Returns:
    - tuple: The maximum sum, top-left corner (i1, j1), and bottom-right corner (i2, j2) of the submatrix.
    """

    # Function to generate a random program (candidate solution) respecting the constraints
    def generate_program(matrix):
        """
        Generates a random program (submatrix indices) respecting the constraints.

        Parameters:
        - matrix (list): The input 2D array represented as a list of lists.

        Returns:
        - tuple: The indices (i1, i2, j1, j2) representing the generated program.
        """
        rows, cols = len(matrix), len(matrix[0])
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
        - matrix (list): The input 2D array represented as a list of lists.

        Returns:
        - int: The fitness value (sum of elements in the submatrix).
        """
        i1, i2, j1, j2 = program
        submatrix = [row[j1:j2 + 1] for row in matrix[i1:i2 + 1]]
        return sum(sum(row) for row in submatrix)

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
        # Sort the population based on fitness
        population = sorted(population, key=lambda program: -fitness(program, matrix))

        # Select the top half of the population
        selected_programs = population[:population_size // 2]

        # Generate new population by recombination and mutation
        new_population = selected_programs.copy()
        while len(new_population) < population_size:
            parent1, parent2 = random.choices(selected_programs, k=2)
            child = recombine(parent1, parent2)
            child = mutate(child, len(matrix), len(matrix[0]))  # Mutate the child program
            new_population.append(child)

        population = new_population

    # Return the program with the maximum fitness (maximum sum of submatrix)
    best_program = max(population, key=lambda program: fitness(program, matrix))
    i1, i2, j1, j2 = best_program
    top_left = (i1, j1)
    bottom_right = (i2, j2)
    max_sum = fitness(best_program, matrix)
    
    return max_sum, top_left, bottom_right