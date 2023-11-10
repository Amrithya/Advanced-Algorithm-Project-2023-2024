import numpy as np
import random
import time
import matplotlib.pyplot as plt

def greedy_algorithm(matrix, k, l):
    """
    Greedy Algorithm to find the maximum segment sum in a 2D matrix with size constraints.

    Parameters:
    - matrix (numpy.ndarray): The 2D matrix for which the maximum segment sum is to be found.
    - k (int): Constraint for the number of rows in the submatrix.
    - l (int): Constraint for the number of columns in the submatrix.

    Returns:
    - tuple: A tuple representing the best solution found, i.e., (i1, i2, j1, j2).
    """
    rows, cols = matrix.shape
    best_solution = None
    best_score = float('-inf')

    for i1 in range(rows - k + 1):
        for i2 in range(i1 + k, rows + 1):
            for j1 in range(cols - l + 1):
                for j2 in range(j1 + l, cols + 1):
                    current_solution = (i1, i2 - 1, j1, j2 - 1)
                    current_score = evaluate_solution(current_solution, matrix)

                    if current_score > best_score:
                        best_solution = current_solution
                        best_score = current_score

    return best_solution

def generate_solution(rows, cols, K, L):
    """
    Generate a random solution (submatrix indices) for the given matrix with shape constraints.

    Parameters:
    - rows (int): Number of rows in the matrix.
    - cols (int): Number of columns in the matrix.
    - K (int): Required number of rows in the submatrix.
    - L (int): Required number of columns in the submatrix.

    Returns:
    - tuple: A tuple representing the random solution (i1, i2, j1, j2).
    """
    i1 = random.randint(0, rows - K)
    i2 = i1 + K - 1
    j1 = random.randint(0, cols - L)
    j2 = j1 + L - 1
    return i1, i2, j1, j2

def crossover(parent1, parent2):
    """
    Perform crossover (recombination) between two parents to generate a child.

    Parameters:
    - parent1 (tuple): First parent representing a solution.
    - parent2 (tuple): Second parent representing a solution.

    Returns:
    - tuple: A tuple representing the child solution.
    """
    # Perform crossover for each index (i1, i2, j1, j2) separately
    child = tuple(random.choice(gene) for gene in zip(parent1, parent2))
    return child

def mutate(solution, rows, cols):
    """
    Mutate a solution by randomly changing one of its genes (index).

    Parameters:
    - solution (tuple): A tuple representing the solution (i1, i2, j1, j2).
    - rows (int): Number of rows in the matrix.
    - cols (int): Number of columns in the matrix.

    Returns:
    - tuple: A tuple representing the mutated solution.
    """
    mutated_gene_index = random.randint(0, 3)
    mutated_gene_value = random.randint(0, rows - 1) if mutated_gene_index < 2 else random.randint(0, cols - 1)
    mutated_solution = list(solution)
    mutated_solution[mutated_gene_index] = mutated_gene_value
    return tuple(mutated_solution)

def genetic_algorithm(matrix, K, L, population_size=20, num_generations=100):
    """
    Genetic Algorithm to find the maximum segment sum in a 2D matrix with shape constraints.

    Parameters:
    - matrix (numpy.ndarray): The 2D matrix for which the maximum segment sum is to be found.
    - K (int): Required number of rows in the submatrix.
    - L (int): Required number of columns in the submatrix.
    - population_size (int): The size of the population (number of individuals in each generation).
    - num_generations (int): The number of generations.

    Returns:
    - tuple: A tuple representing the best solution found, i.e., (i1, i2, j1, j2).
    """
    rows, cols = matrix.shape

    # Generate an initial population of random solutions with shape constraints
    population = [generate_solution(rows, cols, K, L) for _ in range(population_size)]

    for generation in range(num_generations):
        # Evaluate the fitness of each individual in the population
        fitness_scores = [evaluate_solution(individual, matrix) for individual in population]

        # Select the top individuals as parents for crossover
        num_parents = int(0.2 * population_size)
        parents_indices = np.argsort(fitness_scores)[-num_parents:]
        parents = [population[i] for i in parents_indices]

        # Generate offspring through crossover
        offspring = []
        for _ in range(population_size - num_parents):
            parent1 = random.choice(parents)
            parent2 = random.choice(parents)
            child = crossover(parent1, parent2)
            offspring.append(child)

        # Mutate the offspring
        offspring = [mutate(child, rows, cols) for child in offspring]

        # Combine parents and offspring to form the next generation
        population = parents + offspring

    # Select the best individual as the final solution
    best_individual = max(population, key=lambda x: evaluate_solution(x, matrix))

    return best_individual

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
        # Add more test cases as needed
    ]

    k = 2  # Example value for K
    l = 3  # Example value for L

    for test in tests:
        matrix = np.array(test["matrix"])
        # Apply the Genetic Algorithm with size constraints
        start_time_genetic = time.time()
        i1_genetic, i2_genetic, j1_genetic, j2_genetic = genetic_algorithm(matrix, k, l)
        end_time_genetic = time.time()

        max_sum_genetic = matrix[i1_genetic:i2_genetic + 1, j1_genetic:j2_genetic + 1].sum()
        execution_time_genetic = end_time_genetic - start_time_genetic

        # Print the results for Genetic Algorithm
        print("Genetic Algorithm:")
        print(f"Matrix:")
        print(matrix)
        print(f"Maximum Segment Sum: {max_sum_genetic}")
        print(f"Indices (i1, i2, j1, j2): ({i1_genetic}, {i2_genetic}, {j1_genetic}, {j2_genetic}")
        print(f"Execution Time: {execution_time_genetic} seconds")
        print("=" * 30)

        # Plot the matrix for Genetic Algorithm
        plt.xlabel('Algorithms')
        plt.ylabel('Maximum Segment Sum')
        plt.imshow(matrix, cmap='viridis')
        plt.title(f'Original Matrix\nMaximum Segment Sum: {max_sum_genetic}')
        plt.colorbar()
        plt.show()

        # Plot the selected submatrix for Genetic Algorithm
        plt.imshow(matrix[i1_genetic:i2_genetic + 1, j1_genetic:j2_genetic + 1], cmap='viridis')
        plt.title('Selected Submatrix (Genetic Algorithm)')
        plt.colorbar()
        # Annotate the plot with Maximum Segment Sum
        plt.annotate(f'Max Sum: {max_sum_genetic}', xy=(0.5, 0.5), xytext=(30, 10),
                     textcoords='offset points', color='white', fontsize=12, bbox=dict(facecolor='black', alpha=0.7))
        plt.show()


        # Apply the Greedy Algorithm with size constraints
        start_time_greedy = time.time()
        i1_greedy, i2_greedy, j1_greedy, j2_greedy = greedy_algorithm(matrix, k, l)
        end_time_greedy = time.time()

        max_sum_greedy = matrix[i1_greedy:i2_greedy + 1, j1_greedy:j2_greedy + 1].sum()
        execution_time_greedy = end_time_greedy - start_time_greedy

        # Print the results for Greedy Algorithm
        print("Greedy Algorithm:")
        print(f"Matrix:")
        print(matrix)
        print(f"Maximum Segment Sum: {max_sum_greedy}")
        print(f"Indices (i1, i2, j1, j2): ({i1_greedy}, {i2_greedy}, {j1_greedy}, {j2_greedy}")
        print(f"Execution Time: {execution_time_greedy} seconds")
        print("=" * 30)

        # Plot the matrix for Greedy Algorithm
        plt.xlabel('Algorithms')
        plt.ylabel('Maximum Segment Sum')
        plt.imshow(matrix, cmap='viridis')
        plt.title(f'Original Matrix\nMaximum Segment Sum: {max_sum_greedy}')
        plt.colorbar()
        plt.show()

        # Plot the selected submatrix for Greedy Algorithm
        plt.imshow(matrix[i1_greedy:i2_greedy + 1, j1_greedy:j2_greedy + 1], cmap='viridis')
        plt.title('Selected Submatrix (Greedy Algorithm)')
        plt.colorbar()
        # Annotate the plot with Maximum Segment Sum
        plt.annotate(f'Max Sum: {max_sum_greedy}', xy=(0.5, 0.5), xytext=(30, 10),
                     textcoords='offset points', color='white', fontsize=12, bbox=dict(facecolor='black', alpha=0.7))
        plt.show()
# Call the main function
if __name__ == "__main__":
    main()
