import random
# Setting a fixed seed for the random number generator to ensure reproducibility
random.seed(42)

def calculate_subarray_sum(matrix, top, left, K, L):
    """
    Calculate the sum of elements in a KxL subarray within the matrix,
    starting from the top-left corner at (top, left).
    
    Parameters:
    matrix (list of lists): The input matrix.
    top (int): The top row index of the subarray.
    left (int): The left column index of the subarray.
    K (int): The number of rows in the subarray.
    L (int): The number of columns in the subarray.

    Returns:
    int: The sum of elements in the specified subarray.
    """
    sum = 0
    for i in range(top, min(top + K, len(matrix))):
        for j in range(left, min(left + L, len(matrix[0]))):
            sum += matrix[i][j]
    return sum

def create_individual(matrix, K, L):
    """
    Create an individual for the genetic algorithm population.
    An individual represents a subarray with its top-left corner coordinates.
    
    Parameters:
    matrix (list of lists): The input matrix.
    K (int): The number of rows in the subarray.
    L (int): The number of columns in the subarray.

    Returns:
    tuple: A tuple representing the top-left corner (row, column) of a subarray.
    """
    rows, cols = len(matrix), len(matrix[0])
    top = random.randint(0, max(0, rows - K))
    left = random.randint(0, max(0, cols - L))
    return (top, left)

def compute_fitness(individual, matrix, K, L, offset):
    """
    Compute the fitness of an individual.
    The fitness is the sum of the subarray represented by the individual plus an offset.
    
    Parameters:
    individual (tuple): The individual representing a subarray.
    matrix (list of lists): The input matrix.
    K (int): The number of rows in the subarray.
    L (int): The number of columns in the subarray.
    offset (int): A value to be added to the subarray sum for fitness calculation.

    Returns:
    int: The fitness value of the individual.
    """
    top, left = individual
    return calculate_subarray_sum(matrix, top, left, K, L) + offset

def select(population, fitnesses, num_parents):
    """
    Select a subset of the population as parents for the next generation.
    Selection is based on fitness scores.
    
    Parameters:
    population (list of tuples): The current population of individuals.
    fitnesses (list of ints): The fitness scores of the individuals.
    num_parents (int): The number of parents to select.

    Returns:
    list of tuples: The selected parents for the next generation.
    """
    return random.choices(population, weights=fitnesses, k=num_parents)

def mutate(individual, matrix, K, L):
    """
    Mutate an individual by randomly changing its top-left corner.
    Ensures that the subarray stays within the matrix bounds.
    
    Parameters:
    individual (tuple): The individual to mutate.
    matrix (list of lists): The input matrix.
    K (int): The number of rows in the subarray.
    L (int): The number of columns in the subarray.

    Returns:
    tuple: The mutated individual.
    """
    rows, cols = len(matrix), len(matrix[0])
    top, left = individual
    top = random.randint(0, max(0, rows - K))
    left = random.randint(0, max(0, cols - L))
    return (top, left)

def genetic_algorithm(matrix, K, L, num_generations=200, population_size=200, num_parents=100):
    """
    Genetic algorithm to find a subarray of size KxL with the maximum sum in a matrix.
    The algorithm evolves through several generations to optimize the solution.
    
    Parameters:
    matrix (list of lists): The input matrix.
    K (int): The number of rows in the subarray.
    L (int): The number of columns in the subarray.
    num_generations (int): The number of generations for the algorithm to run.
    population_size (int): The number of individuals in each generation.
    num_parents (int): The number of parents to select for breeding.

    Returns:
    tuple: A tuple containing the maximum sum, top-left and bottom-right coordinates of the subarray.
    """
    # Calculate offset to ensure fitness is always positive
    min_element = min(min(row) for row in matrix)
    offset = -min_element * K * L if min_element < 0 else 0

    # Initialize population
    population = [create_individual(matrix, K, L) for _ in range(population_size)]

    # Evolve the population over generations
    for generation in range(num_generations):
        fitnesses = [compute_fitness(individual, matrix, K, L, offset) for individual in population]
        parents = select(population, fitnesses, num_parents)
        next_population = [mutate(random.choice(parents), matrix, K, L) for _ in range(population_size)]
        population = next_population

    # Find the best solution
    best_individual = max(population, key=lambda ind: compute_fitness(ind, matrix, K, L, offset))
    top, left = best_individual
    top_left = (top, left)
    bottom, right = top + K - 1, left + L - 1
    bottom_right = (bottom, right)
    max_sum = calculate_subarray_sum(matrix, top, left, K, L)
    return max_sum, top_left, bottom_right
