import numpy as np  # Importing the numpy library as 'np' for efficient numerical operations.
import random  # Importing the 'random' module to generate random numbers.
import time
import matplotlib.pyplot as plt

#  Génétic Algorithms
def max_segment_2d_genetic(matrix, population_size=100, num_generations=100):
    def generate_program(matrix):
        rows, cols = matrix.shape
        i1 = random.randint(0, rows - 1)
        i2 = random.randint(i1, rows - 1)
        j1 = random.randint(0, cols - 1)
        j2 = random.randint(j1, cols - 1)
        return i1, i2, j1, j2

    def fitness(program, matrix):
        i1, i2, j1, j2 = program
        submatrix = matrix[i1:i2 + 1, j1:j2 + 1]
        return np.sum(submatrix)

    def recombine(program1, program2):
        i1 = (program1[0] + program2[0]) // 2
        i2 = (program1[1] + program2[1]) // 2
        j1 = (program1[2] + program2[2]) // 2
        j2 = (program1[3] + program2[3]) // 2
        return i1, i2, j1, j2

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

    population = [generate_program(matrix) for _ in range(population_size)]

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

    return max(population, key=lambda program: fitness(program, matrix))

# Fonction pour générer une solution initiale (sous-matrice aléatoire)
def generate_solution(matrix):
    rows, cols = matrix.shape
    i1 = random.randint(0, rows - 1)
    i2 = random.randint(i1, rows - 1)
    j1 = random.randint(0, cols - 1)
    j2 = random.randint(j1, cols - 1)
    return i1, i2, j1, j2

# Fonction pour évaluer une solution (somme des éléments de la sous-matrice)
def evaluate_solution(solution, matrix):
    i1, i2, j1, j2 = solution
    submatrix = matrix[i1:i2 + 1, j1:j2 + 1]
    return np.sum(submatrix)


import time
import matplotlib.pyplot as plt

def plot_algorithm_comparison(algorithm_names, max_sums, algorithm_name):
    plt.figure(figsize=(8, 6))
    plt.scatter(algorithm_names, max_sums, color='red', marker='o')
    plt.xlabel('Algorithms')
    plt.ylabel('Maximum Segment Sum')
    plt.title(f'Maximum Segment Sum Comparison - {algorithm_name}')
    plt.grid(True)  # Ajout d'une grille
    plt.show()

def main():
    matrix = np.array([[1, 2, -1, -4, -20],
                      [-8, -3, 4, 2, 1],
                      [3, 8, 10, 1, 3],
                      [-4, -1, 1, 7, -6]])

    # Genetic Programming
    start_time = time.time()
    i1_genetic, i2_genetic, j1_genetic, j2_genetic = max_segment_2d_genetic(matrix)
    max_sum_genetic = matrix[i1_genetic:i2_genetic + 1, j1_genetic:j2_genetic + 1].sum()
    end_time = time.time()
    print("Genetic Programming:")
    print(f"Maximum Segment Sum: {max_sum_genetic}")
    print(f"Indices (i1, i2, j1, j2): ({i1_genetic}, {i2_genetic}, {j1_genetic}, {j2_genetic}")
    print(f"Execution Time: {end_time - start_time} seconds")
    print("="*30)

    # Plotting comparison
    algorithm_names = ["Genetic Programming"]
    max_sums = [max_sum_genetic]
    algorithm_name = "Genetic Programming"
    plot_algorithm_comparison(algorithm_names, max_sums, algorithm_name)

# call fonction main
if __name__ == "__main__":
    main()
