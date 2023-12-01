import random
import sys
import os
import random
import sys
import os
import time
import numpy as np

# sys.path
project_directory = 'C:/Users/youss/OneDrive/Bureau/Adavance Algorithm/Advanced-Algorithm-Project-2023-2024'
sys.path.append(project_directory)


from genetic_algorithm.genetic_algorithm_no_constraint import max_segment_2d_genetic
from genetic_algorithm.genetic_algorithm_with_constraint import genetic_algorithm as genetic_algorithm_constrained

from genetic_algorithm.genetic_algorithm_no_constraint import evaluate_solution

from ant_colony_approach.ant_colony_algorithm_no_constraint import  ant_colony_algorithm
from ant_colony_approach.ant_colony_algorithm_with_constraint import  ant_colony_optimization


# Function to generate a random matrix as a NumPy array
def generate_matrix(rows, cols, value_range):
    return np.random.randint(value_range[0], value_range[1], (rows, cols))

# Function to save a matrix to a file
def save_matrix_to_file(matrix, file_path):
    with open(file_path, 'w') as file:
        for row in matrix:
            line = ' '.join(str(val) for val in row)
            file.write(line + '\n')

# Function to read a matrix from a file
def read_matrix_from_file(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            row = [int(val) for val in line.split()]
            matrix.append(row)
    return matrix

# Add the path of the 'genetic_algorithm' folder's parent directory to sys.path
project_directory = 'C:/Users/youss/OneDrive/Bureau/Adavance Algorithm/Advanced-Algorithm-Project-2023-2024'
sys.path.append(project_directory)


def main():

    # Generate different matrices
    low_dimensional_matrix = generate_matrix(3, 3, (-10, 10))
    large_scale_matrix = generate_matrix(50, 50, (-25, 25))
    grand_scale_matrix = generate_matrix(100, 100, (-50, 50))

    # File paths for each matrix
    low_dim_path = os.path.join(project_directory, 'genetic_algorithm/low_dimensional.txt')
    large_scale_path = os.path.join(project_directory, 'genetic_algorithm/large_scale.txt')
    grand_scale_path = os.path.join(project_directory, 'genetic_algorithm/grand_scale.txt')

    # Save each matrix to its respective file
    save_matrix_to_file(low_dimensional_matrix, low_dim_path)
    save_matrix_to_file(large_scale_matrix, large_scale_path)
    save_matrix_to_file(grand_scale_matrix, grand_scale_path)

    # Read and test each matrix from its file
    matrix_ld = read_matrix_from_file(low_dim_path)
    matrix_ls = read_matrix_from_file(large_scale_path)
    matrix_gs = read_matrix_from_file(grand_scale_path)


   
    K, L = 2, 2  # Dimensions du sous-tableau à chercher
    # Print the matrix
    print("Matrix_ld:")
    for row in matrix_ld:
        print(row)
    print("K:", K,"L:", L)

    # Execute the Genetic Algorithm without constraint
    # Convert the list to a numpy array
    numpy_matrix = np.array(matrix_ld)

    # Apply the genetic algorithm
    start_time = time.time()
    result = max_segment_2d_genetic(numpy_matrix, population_size=100, num_generations=100)
    end_time = time.time()

    # Display the matrix and the result
    print("Matrix:")
    print(numpy_matrix)
    print("\nIndices of the maximal sub-matrix: ", result)

    i1, i2, j1, j2 = result
    submatrix_sum = evaluate_solution(result, numpy_matrix)
    print("Sum of the maximal sub-matrix Genetic Algorithm without constraint:", submatrix_sum)
    print("Maximal sub-matrix Genetic Algorithm without constraint:\n", numpy_matrix[i1:i2 + 1, j1:j2 + 1])
    print("\nTemps d'exécution Genetic Algorithm without constraint:", end_time - start_time, "secondes")
    # result_gen, top_left_gen, bottom_right_gen = max_segment_2d_genetic (matrix)
    # print("Genetic Algorithm:", result_gen, top_left_gen, bottom_right_gen)

    # Execute the Genetic Algorithm with constraint
    result_gen_constrained, top_left_gen_constrained, bottom_right_gen_constrained = genetic_algorithm_constrained(matrix_ld, K, L,100,50, 10)
    print("Genetic Algorithm with Constraint:", result_gen_constrained, top_left_gen_constrained, bottom_right_gen_constrained)

    # Execute the Ant Colony Algorithm without constraint
    result_ant_colony = ant_colony_algorithm(numpy_matrix)
    print("Ant Colony Algorithm without:", result_ant_colony)

    # Execute the Ant Colony Algorithm with constraint
    num_ants = 10
    num_iterations = 100
    evaporation_rate = 0.5

    result, top_left, bottom_right = ant_colony_optimization(matrix_ld, K, L, num_ants, num_iterations, evaporation_rate)
    print("Maximum Subarray Sum:", result)
    print("Top Left Index of Subarray:", top_left)
    print("Bottom Right Index of Subarray:", bottom_right)
 
    result_ant_colony_opt = ant_colony_optimization(matrix_ld, K, L, num_ants, num_iterations, evaporation_rate)
    print("Ant Colony Optimization with Constraint:", result_ant_colony_opt)


if __name__ == "__main__":
    main()