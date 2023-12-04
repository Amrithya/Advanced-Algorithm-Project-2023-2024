import os
import random
import time
import matplotlib.pyplot as plt
from genetic_algorithm.genetic_algorithm_no_constraint import max_segment_2d_genetic
from genetic_algorithm.genetic_algorithm_with_constraint import genetic_algorithm as genetic_algorithm_constrained
from ant_colony_approach.ant_colony_algorithm_no_constraint import ant_colony_algorithm
from ant_colony_approach.ant_colony_algorithm_with_constraint import ant_colony_optimization
from ant_colony_approach.ant_colony_algorithm_with_constraint import ant_colony_optimization
random.seed(42)  # Set a random seed for reproducibility

      
# Define your project directory
project_directory = 'C:/Users/youss/OneDrive/Bureau/Adavance Algorithm/Advanced-Algorithm-Project-2023-2024'
# Define functions for matrix generation, saving, and reading
def generate_matrix(rows, cols, value_range):
    return [[random.randint(value_range[0], value_range[1]) for _ in range(cols)] for _ in range(rows)]

def save_matrix_to_file(matrix, file_path):
    with open(file_path, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

def read_matrix_from_file(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            row = list(map(int, line.split()))
            matrix.append(row)
    return matrix

# Define the complexity calculation function
def calculate_complexity(matrix_size, algorithm_type, P_G=None, A_I=None, K=None, L=None):
    if algorithm_type == "genetic_no_constraint":
        P, G = P_G if P_G else (100, 50)  # Default values or use provided values
        return P * G * matrix_size ** 2  # O(P × G × N^2)
    elif algorithm_type == "ant_colony_no_constraint":
        A, I = A_I if A_I else (200, 100)  # Default values or use provided values
        return A * I * matrix_size ** 2  # O(A × I × N^2)
    elif algorithm_type == "genetic_constrained" or algorithm_type == "ant_colony_constrained":
        P = G = A = I = 100  # Placeholder values for population size and generations/iterations
        return P * G * K * L if algorithm_type.startswith("genetic") else A * I * K * L  # O(P × G × K × L) or O(A × I × K × L)
    return 0

# Main function
def main():
    # Define your project directory
    project_directory = 'C:/Users/youss/OneDrive/Bureau/Adavance Algorithm/Advanced-Algorithm-Project-2023-2024/Plot genetic_ant_algorithm'

    matrices = {
        'small_matrix': generate_matrix(5, 5, (-10, 10)),
        'medium_matrix': generate_matrix(10, 10, (-20, 20)),
        'large_matrix': generate_matrix(20, 20, (-50, 50))
    }

    times_no_constraint = []
    times_constrained = []
    times_ant_colony_no_constraint=[]
    times_ant_colony_constrained=[]
    complexities_no_constraint = []
    complexities_constrained = []
    complexities_ant_colony_no_constraint=[]
    complexities_ant_colony_constrained=[]
   
    for matrix_label, matrix in matrices.items():
        K, L = 3, 3  # Example values for constrained algorithms

        file_path = os.path.join(project_directory, f"{matrix_label}.txt")
        save_matrix_to_file(matrix, file_path)
        matrix_from_file = read_matrix_from_file(file_path)

        # Genetic Algorithm (No Constraint)
        start_time = time.time()
        result_no_constraint = max_segment_2d_genetic(matrix_from_file)
        times_no_constraint.append(time.time() - start_time)
        complexities_no_constraint.append(calculate_complexity(len(matrix), "genetic_no_constraint"))

        # Genetic Algorithm (Constrained)
        start_time = time.time()
        result_constrained = genetic_algorithm_constrained(matrix_from_file, K, L)
        times_constrained.append(time.time() - start_time)
        complexities_constrained.append(calculate_complexity(len(matrix), "genetic_constrained", K=K, L=L))

        # Ant Colony Algorithm (No Constraint)
        start_time = time.time()
        ant_colony_result_no_constraint = ant_colony_algorithm(matrix_from_file)
        times_ant_colony_no_constraint.append(time.time() - start_time)
        complexities_ant_colony_no_constraint.append(calculate_complexity(len(matrix), "ant_colony_no_constraint"))

        # Ant Colony Algorithm (Constrained)
        start_time = time.time()
        ant_colony_result_constrained = ant_colony_optimization(matrix_from_file, K, L)
        times_ant_colony_constrained.append(time.time() - start_time)
        complexities_ant_colony_constrained.append(calculate_complexity(len(matrix), "ant_colony_constrained", K=K, L=L))
        
        # Print results for Genetic Algorithm
        print(f"Results for {matrix_label}:")
        print(f"Genetic Algorithm (No Constraint): {result_no_constraint}, Time: {times_no_constraint[-1]}")
        print(f"Genetic Algorithm (Constrained): {result_constrained}, Time: {times_constrained[-1]}")
        # Print results for Ant Colony Algorithm
        print(f"Ant Colony (No Constraint): {ant_colony_result_no_constraint}, Time: {times_ant_colony_no_constraint[-1]}")
        print(f"Ant Colony (Constrained): {ant_colony_result_constrained}, Time: {times_ant_colony_constrained[-1]}")

   
    # Plotting execution times
    matrix_sizes = ['Small', 'Medium', 'Large']
    plt.figure(figsize=(10, 6))
    plt.plot(matrix_sizes, times_no_constraint, label='Genetic Algorithm No Constraint', marker='o')
    plt.plot(matrix_sizes, times_constrained, label='Genetic Algorithm Constrained', marker='o')
    plt.plot(matrix_sizes, times_ant_colony_no_constraint, label='Ant Colony No Constraint', marker='o')
    plt.plot(matrix_sizes, times_ant_colony_constrained, label='Ant Colony Constrained', marker='o')
    plt.title("Execution Times of Algorithms on Different Matrix Sizes")
    plt.xlabel('Matrix Size')
    plt.ylabel('Execution Time (Seconds)')
    plt.legend()
    plt.savefig(os.path.join(project_directory, "execution_times_comparison.png"))
    plt.show()

    # Plotting complexities
    plt.figure(figsize=(10, 6))
    plt.plot(matrix_sizes, complexities_no_constraint, label='Genetic Algorithm No Constraint', marker='x')
    plt.plot(matrix_sizes, complexities_constrained, label='Genetic Algorithm Constrained', marker='x')

    plt.plot(matrix_sizes, complexities_ant_colony_no_constraint, label='Ant Colony No Constraint', marker='x')
    plt.plot(matrix_sizes, complexities_ant_colony_constrained, label='Ant Colony Constrained', marker='x')
 
    plt.title("Algorithm Complexities on Different Matrix Sizes")
    plt.xlabel('Matrix Size')
    plt.ylabel('Complexity')
    plt.legend()
    plt.savefig(os.path.join(project_directory, "complexities_comparison.png"))
    plt.show()
 # Define the list of algorithms
    algorithms = ['Genetic No Constraint', 'Genetic Constrained', 
                  'Ant Colony No Constraint', 'Ant Colony Constrained']

    for algorithm in algorithms:
        # Corrected data extraction logic for each algorithm
        if algorithm == 'Genetic No Constraint':
            execution_times = times_no_constraint
            complexities = complexities_no_constraint
        elif algorithm == 'Genetic Constrained':
            execution_times = times_constrained
            complexities = complexities_constrained
        elif algorithm == 'Ant Colony No Constraint':
            execution_times = times_ant_colony_no_constraint
            complexities = complexities_ant_colony_no_constraint
        elif algorithm == 'Ant Colony Constrained':
            execution_times = times_ant_colony_constrained
            complexities = complexities_ant_colony_constrained

        # Plotting execution times for each algorithm
        plt.figure(figsize=(10, 6))
        plt.plot(matrix_sizes, execution_times, label=f'Execution Times - {algorithm}', marker='o')
        plt.title(f"Execution Times for {algorithm}")
        plt.xlabel('Matrix Size')
        plt.ylabel('Execution Time (Seconds)')
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(project_directory, f"execution_time_{algorithm.replace(' ', '_').lower()}.png"))
        plt.close()

        # Plotting complexities for each algorithm
        plt.figure(figsize=(10, 6))
        plt.plot(matrix_sizes, complexities, label=f'Complexities - {algorithm}', marker='x')
        plt.title(f"Algorithm Complexities for {algorithm}")
        plt.xlabel('Matrix Size')
        plt.ylabel('Complexity')
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(project_directory, f"complexity_{algorithm.replace(' ', '_').lower()}.png"))
        plt.close()


if __name__ == "__main__":
    main()