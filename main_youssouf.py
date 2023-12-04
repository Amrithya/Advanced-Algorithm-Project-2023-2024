import os
import random
import time
import matplotlib.pyplot as plt
import numpy as np
from genetic_algorithm.genetic_algorithm_no_constraint import max_segment_2d_genetic
from genetic_algorithm.genetic_algorithm_with_constraint import genetic_algorithm as genetic_algorithm_constrained
from ant_colony_approach.ant_colony_algorithm_no_constraint import ant_colony_algorithm
from ant_colony_approach.ant_colony_algorithm_with_constraint import ant_colony_optimization

# Set a fixed random seed for reproducibility
random.seed(42)

# Get the current working directory (project root directory)
root_directory = os.getcwd()

# Create 'genetic_algorithm' directory in the root directory if it doesn't exist
project_directory = os.path.join(root_directory, 'genetic_algorithm')
os.makedirs(project_directory, exist_ok=True)

# Function to generate a matrix with random values
def generate_matrix(rows, cols, value_range):
    return [[random.randint(value_range[0], value_range[1]) for _ in range(cols)] for _ in range(rows)]

# Function to save a matrix to a file
def save_matrix_to_file(matrix, file_path):
    with open(file_path, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

# Function to read a matrix from a file
def read_matrix_from_file(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            row = list(map(int, line.split()))
            matrix.append(row)
    return matrix
def plot_bar_chart(matrix_sizes, times, title, filename):
    # Preparing data for the bar chart
    labels = matrix_sizes
    # Extracting data for each algorithm
    genetic_no_constraint = [times['Genetic Algorithm No Constraint'][i] for i in range(len(matrix_sizes))]
    genetic_constrained = [times['Genetic Algorithm Constrained'][i] for i in range(len(matrix_sizes))]
    ant_colony_no_constraint = [times['Ant Colony No Constraint'][i] for i in range(len(matrix_sizes))]
    ant_colony_constrained = [times['Ant Colony Constrained'][i] for i in range(len(matrix_sizes))]

    x = np.arange(len(labels))  # Label positions
    width = 0.2  # Width of the bars

    fig, ax = plt.subplots(figsize=(12, 6))
    # Plotting bars for each algorithm
    rects1 = ax.bar(x - width*1.5, genetic_no_constraint, width, label='Genetic No Constraint')
    rects2 = ax.bar(x - width/2, genetic_constrained, width, label='Genetic Constrained')
    rects3 = ax.bar(x + width/2, ant_colony_no_constraint, width, label='Ant Colony No Constraint')
    rects4 = ax.bar(x + width*1.5, ant_colony_constrained, width, label='Ant Colony Constrained')

    # Adding text for labels, title, and custom x-axis tick labels
    ax.set_ylabel('Execution Time (Seconds)')
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    # Attaching annotations to each bar
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{height:.2f}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)
    autolabel(rects4)

    fig.tight_layout()
    plt.savefig(os.path.join(project_directory, filename))
    plt.show()

def plot_complexity_bar_chart(matrix_sizes, complexities, title, filename):
    # Preparing data for the bar chart
    labels = matrix_sizes
    # Extracting data for each algorithm
    genetic_no_constraint = [complexities['Genetic Algorithm No Constraint'][i] for i in range(len(matrix_sizes))]
    genetic_constrained = [complexities['Genetic Algorithm Constrained'][i] for i in range(len(matrix_sizes))]
    ant_colony_no_constraint = [complexities['Ant Colony No Constraint'][i] for i in range(len(matrix_sizes))]
    ant_colony_constrained = [complexities['Ant Colony Constrained'][i] for i in range(len(matrix_sizes))]

    x = np.arange(len(labels))  # Label positions
    width = 0.2  # Width of the bars

    fig, ax = plt.subplots(figsize=(12, 6))
    # Plotting bars for each algorithm
    rects1 = ax.bar(x - width*1.5, genetic_no_constraint, width, label='Genetic No Constraint')
    rects2 = ax.bar(x - width/2, genetic_constrained, width, label='Genetic Constrained')
    rects3 = ax.bar(x + width/2, ant_colony_no_constraint, width, label='Ant Colony No Constraint')
    rects4 = ax.bar(x + width*1.5, ant_colony_constrained, width, label='Ant Colony Constrained')

    # Adding text for labels, title, and custom x-axis tick labels
    ax.set_ylabel('Complexity')
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    # Attaching annotations to each bar
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{height:.2f}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)
    autolabel(rects4)

    fig.tight_layout()
    plt.savefig(os.path.join(project_directory, filename))
    plt.show()

# Function to calculate complexity based on algorithm type
def calculate_complexity(matrix_size, algorithm_type, P_G=None, A_I=None, K=None, L=None):
    N, M = matrix_size

    if algorithm_type == "genetic_no_constraint":
        P, G = P_G if P_G else (100, 50)
        return P * G * N * M  # O(P × G × N × M)

    elif algorithm_type == "genetic_constrained":
        P, G = P_G if P_G else (100, 50)
        return P * G * (N * M + K * L)  # O(P × G × (N × M + K × L))

    elif algorithm_type == "ant_colony_no_constraint":
        A, I = A_I if A_I else (200, 100)
        return N * M * A * I  # O(N × M × A × I)

    elif algorithm_type == "ant_colony_constrained":
        A, I = A_I if A_I else (200, 100)
        return N * M * A * I * K * L  # O(N × M × A × I × K × L)

    return 0

# Main function to execute the algorithms and plot results
def main():
    matrices = {
        'small_matrix': generate_matrix(5, 5, (-10, 10)),
        'medium_matrix': generate_matrix(10, 10, (-20, 20)),
        'large_matrix': generate_matrix(10, 10, (-15, 15))
    }

    # Initialize data storage for execution times and complexities
    times_no_constraint = []
    times_constrained = []
    times_ant_colony_no_constraint = []
    times_ant_colony_constrained = []
    complexities_no_constraint = []
    complexities_constrained = []
    complexities_ant_colony_no_constraint = []
    complexities_ant_colony_constrained = []

    # Initialize lists to store results from each algorithm
    results_genetic_no_constraint = []
    results_genetic_constrained = []
    results_ant_colony_no_constraint = []
    results_ant_colony_constrained = []

    
    # Process each matrix and calculate times and complexities
     # Process each matrix
    for matrix_label, matrix in matrices.items():
        # Example values for constrained algorithms
        K, L = 2, 2  

        # Save and read matrix from file
        file_path = os.path.join(project_directory, f"{matrix_label}.txt")
        save_matrix_to_file(matrix, file_path)
        matrix_from_file = read_matrix_from_file(file_path)


    
        # Calculate and store results and times for the Genetic Algorithm (No Constraint)
        start_time = time.time()
        result = max_segment_2d_genetic(matrix)
        end_time = time.time()
        results_genetic_no_constraint.append(result)
        times_no_constraint.append(end_time - start_time)
        complexities_no_constraint.append(calculate_complexity((len(matrix), len(matrix[0])), "genetic_no_constraint"))

        # Calculate and store results and times for the Genetic Algorithm (Constrained)
        start_time = time.time()
        result = genetic_algorithm_constrained(matrix, K, L)
        end_time = time.time()
        results_genetic_constrained.append(result)
        times_constrained.append(end_time - start_time)
        complexities_constrained.append(calculate_complexity((len(matrix), len(matrix[0])), "genetic_constrained", K=K, L=L))

        # Calculate and store results and times for the Ant Colony Algorithm (No Constraint)
        start_time = time.time()
        result = ant_colony_algorithm(matrix)
        end_time = time.time()
        results_ant_colony_no_constraint.append(result)
        times_ant_colony_no_constraint.append(end_time - start_time)
        complexities_ant_colony_no_constraint.append(calculate_complexity((len(matrix), len(matrix[0])), "ant_colony_no_constraint"))

        # Calculate and store results and times for the Ant Colony Algorithm (Constrained)
        start_time = time.time()
        result = ant_colony_optimization(matrix, K, L)
        end_time = time.time()
        results_ant_colony_constrained.append(result)
        times_ant_colony_constrained.append(end_time - start_time)
        complexities_ant_colony_constrained.append(calculate_complexity((len(matrix), len(matrix[0])), "ant_colony_constrained", K=K, L=L))

     
    # Process each matrix
    for matrix_label, matrix in matrices.items():
    
        results_genetic_no_constraint.append(max_segment_2d_genetic(matrix))
        results_genetic_constrained.append(genetic_algorithm_constrained(matrix, K, L))
        results_ant_colony_no_constraint.append(ant_colony_algorithm(matrix))
        results_ant_colony_constrained.append(ant_colony_optimization(matrix, K, L))

    # Print results for each matrix size
    matrix_sizes = ['Small', 'Medium', 'Large']
    for i, matrix_size in enumerate(matrix_sizes):
        print(f"Results for {matrix_size} Matrix:")
        print(f"Genetic Algorithm (No Constraint): Result: {results_genetic_no_constraint[i]}, Time: {times_no_constraint[i]}s, Complexity: {complexities_no_constraint[i]}")
        print(f"Genetic Algorithm (Constrained): Result: {results_genetic_constrained[i]}, Time: {times_constrained[i]}s, Complexity: {complexities_constrained[i]}")
        print(f"Ant Colony (No Constraint): Result: {results_ant_colony_no_constraint[i]}, Time: {times_ant_colony_no_constraint[i]}s, Complexity: {complexities_ant_colony_no_constraint[i]}")
        print(f"Ant Colony (Constrained): Result: {results_ant_colony_constrained[i]}, Time: {times_ant_colony_constrained[i]}s, Complexity: {complexities_ant_colony_constrained[i]}")

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

    # Preparing data for visualization
    execution_times = {
        'Genetic Algorithm No Constraint': times_no_constraint,
        'Genetic Algorithm Constrained': times_constrained,
        'Ant Colony No Constraint': times_ant_colony_no_constraint,
        'Ant Colony Constrained': times_ant_colony_constrained
    }

    complexities_data = {
        'Genetic Algorithm No Constraint': complexities_no_constraint,
        'Genetic Algorithm Constrained': complexities_constrained,
        'Ant Colony No Constraint': complexities_ant_colony_no_constraint,
        'Ant Colony Constrained': complexities_ant_colony_constrained
    }

    # Call the function to plot the bar chart for execution times
    plot_bar_chart(matrix_sizes, execution_times, "Execution Times Comparison", "execution_times_comparison")

    # Call the function to plot the bar chart for complexities
    plot_complexity_bar_chart(matrix_sizes, complexities_data, "Complexities Comparison", "complexities_comparison")


# Ensure the main function is executed only when the script is run directly
if __name__ == "__main__":
    main()