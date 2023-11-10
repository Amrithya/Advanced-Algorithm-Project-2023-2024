import numpy as np  # Importing the numpy library as 'np' for efficient numerical operations.
import random  # Importing the 'random' module to generate random numbers.
import time  # Importing the 'time' module to measure execution time.
import matplotlib.pyplot as plt  # Importing the 'matplotlib.pyplot' module for data visualization.

# Genetic Algorithms
def max_segment_2d_genetic(matrix, population_size=100, num_generations=100):
    # Function to generate a random program (candidate solution)
    def generate_program(matrix):
        rows, cols = matrix.shape
        i1 = random.randint(0, rows - 1)
        i2 = random.randint(i1, rows - 1)
        j1 = random.randint(0, cols - 1)
        j2 = random.randint(j1, cols - 1)
        return i1, i2, j1, j2

    # Function to evaluate the fitness of a program
    def fitness(program, matrix):
        i1, i2, j1, j2 = program
        submatrix = matrix[i1:i2 + 1, j1:j2 + 1]
        return np.sum(submatrix)

    # Function to recombine two programs
    def recombine(program1, program2):
        i1 = (program1[0] + program2[0]) // 2
        i2 = (program1[1] + program2[1]) // 2
        j1 = (program1[2] + program2[2]) // 2
        j2 = (program1[3] + program2[3]) // 2
        return i1, i2, j1, j2

    # Function to mutate a program
    def mutate(program):
        i1, i2, j1, j2 = program
        if random.random() < 0.2:
            i1 = random.randint(0, i2)
        if random.random() < 0.2:
            i2 = random.randint(i1, i2)
        if random.random() < 0.2:
            j1 = random.randint(0, j2)
        if random.random() < 0.2:
            j2 = random.randint(j1, j2)
        return i1, i2, j1, j2

    # Initialization of the population with random programs
    population = [generate_program(matrix) for _ in range(population_size)]

    # Main loop for genetic algorithm
    for generation in range(num_generations):
        population = sorted(population, key=lambda program: -fitness(program, matrix))

        selected_programs = population[:population_size // 2]

        new_population = selected_programs.copy()
        while len(new_population) < population_size:
            parent1, parent2 = random.choices(selected_programs, k=2)
            child = recombine(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

    # Return the program with the maximum fitness (maximum sum of submatrix)
    return max(population, key=lambda program: fitness(program, matrix))

# Function to generate an initial solution (random submatrix)
def generate_solution(matrix):
    rows, cols = matrix.shape
    i1 = random.randint(0, rows - 1)
    i2 = random.randint(i1, rows - 1)
    j1 = random.randint(0, cols - 1)
    j2 = random.randint(j1, cols - 1)
    return i1, i2, j1, j2

# Function to evaluate a solution (sum of elements in the submatrix)
def evaluate_solution(solution, matrix):
    i1, i2, j1, j2 = solution
    submatrix = matrix[i1:i2 + 1, j1:j2 + 1]
    return np.sum(submatrix)

# Main function
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

    # Iterate through the test cases
    for test in tests:
        matrix = np.array(test["matrix"])

        # Apply the genetic algorithm
        start_time = time.time()
        i1_genetic, i2_genetic, j1_genetic, j2_genetic = max_segment_2d_genetic(matrix)
        end_time = time.time()

        max_sum_genetic = matrix[i1_genetic:i2_genetic + 1, j1_genetic:j2_genetic + 1].sum()
        execution_time_genetic = end_time - start_time

        # Print the results in a similar format to the provided example
        print("Genetic Programming:")
        print(f"Matrix:")
        print(matrix)
        print(f"Maximum Segment Sum: {max_sum_genetic}")
        print(f"Indices (i1, i2, j1, j2): ({i1_genetic}, {i2_genetic}, {j1_genetic}, {j2_genetic}")
        print(f"Execution Time: {execution_time_genetic} seconds")
        print("=" * 30)

        # Plot the matrix
        plt.xlabel('Algorithms')
        plt.ylabel('Maximum Segment Sum')
        plt.imshow(matrix, cmap='viridis')
        plt.title(f'Original Matrix\nMaximum Segment Sum: {max_sum_genetic}')
        plt.colorbar()
        plt.show()

        # Plot the selected submatrix
        plt.imshow(matrix[i1_genetic:i2_genetic + 1, j1_genetic:j2_genetic + 1], cmap='viridis')
        plt.title('Selected Submatrix')
        plt.colorbar()
        # Annotate the plot with Maximum Segment Sum
        plt.annotate(f'Max Sum: {max_sum_genetic}', xy=(0.5, 0.5), xytext=(30, 10),
                     textcoords='offset points', color='white', fontsize=12, bbox=dict(facecolor='black', alpha=0.7))
        plt.show()

# Call the main function
if __name__ == "__main__":
    main()


