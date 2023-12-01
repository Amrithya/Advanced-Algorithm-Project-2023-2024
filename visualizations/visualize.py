import matplotlib.pyplot as plt

def plot_time_vs_size(data,algorithm_name):
    """
    Plot a line graph where the x-axis represents the size of the matrix (rows x columns) and
    the y-axis represents the time taken for the test case.

    :param data: A sorted array of tuples [(time_for_test_case, size_of_matrix), ...].
    :param algorithm_name: The name of the algorithm
    """
    # Unpacking the data into two separate lists

    times, sizes = zip(*data)


    # Creating the plot
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='o')

    # Setting the labels and title
    plt.xlabel('Size of Matrix (rows x columns)')
    plt.ylabel('Time for Test Case (s)')
    plt.title(f'Time vs Size of Matrix using {algorithm_name} ')

    # Displaying the plot
    plt.show()




