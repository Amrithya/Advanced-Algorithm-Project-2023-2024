import random
random.seed(42)  # Set a random seed for reproducibility

def calculate_subarray_sum(matrix, top, left, K, L):
    """
    Calculate the sum of elements in a KxL subarray within the matrix,
    starting from the top-left corner at (top, left).
    """
    sum = 0
    for i in range(top, min(top + K, len(matrix))):
        for j in range(left, min(left + L, len(matrix[0]))):
            sum += matrix[i][j]
    return sum

def create_individual(matrix, K, L):
    """
    Create an individual for the genetic algorithm population.
    An individual represents a subarray with its top-left corner.
    """
     
    
    rows, cols = len(matrix), len(matrix[0])
    top, left = random.randint(0, rows - K), random.randint(0, cols - L)
    return (top, left)

def compute_fitness(individual, matrix, K, L, offset):
    """
    Compute the fitness of an individual.
    The fitness is the sum of the subarray represented by the individual plus an offset.
    """
    top, left = individual
    return calculate_subarray_sum(matrix, top, left, K, L) + offset

def select(population, fitnesses, num_parents):
    """
    Select a subset of the population as parents for the next generation.
    Selection is based on fitness scores.
    """
    return random.choices(population, weights=fitnesses, k=num_parents)

def mutate(individual, matrix, K, L):
    """
    Mutate an individual by randomly changing its top-left corner.
    Ensures that the subarray stays within the matrix bounds.
    """
    rows, cols = len(matrix), len(matrix[0])
    top, left = individual
    top = random.randint(0, max(0, rows - K))
    left = random.randint(0, max(0, cols - L))
    return (top, left)

def genetic_algorithm(matrix, K, L, num_generations, population_size, num_parents):
    """
    Genetic algorithm to find a subarray of size KxL with the maximum sum in a matrix.
    The algorithm evolves through several generations to optimize the solution.
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
    bottom, right = top + K - 1, left + L - 1
    return calculate_subarray_sum(matrix, top, left, K, L), (top, left), (bottom, right)

# Example usage
matrix = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

# Print the matrix
print("Matrix:")
for row in matrix:
    print(row)

K, L = 1, 1  # Subarray size constraints
result, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y) = genetic_algorithm(matrix, K, L, num_generations=100, population_size=50, num_parents=10)
print("\nMaximum Subarray Sum:", result)
print("Top Left Index:", (top_left_x, top_left_y))
print("Bottom Right Index:", (bottom_right_x, bottom_right_y))
