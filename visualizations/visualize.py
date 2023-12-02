

import matplotlib.pyplot as plt
import numpy as np


def create_test_result_plots(test_results, algorithm_name):
    constraints = test_results['constraints']
    constraints_type = test_results['constraints_type']
    size_run_time_test = test_results['size_run_time_test']
    
    

    # Bar Chart for Successes, Failures, and Skipped
    labels = ['Successes', 'Failures', 'Skipped']
    counts = [test_results['successes'], test_results['failures'], test_results['skipped']]
    plt.figure(figsize=(8, 5))
    plt.bar(labels, counts, color=['green', 'red', 'yellow'])
    plt.title(f'Test Results for {algorithm_name}')
    plt.xlabel('Test Result')
    plt.ylabel('Number of Test Cases')
    plt.show()

    # Percentage Pie Chart
    labels = ['Successes', 'Failures']
    sizes = [test_results['successes'], test_results['failures']]
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['green', 'red'], startangle=90)
    plt.title(f'Test Results Percentage for {algorithm_name}')
    plt.show()

    # line plot for Size vs. Run Time


    # if constraints and constraints_type == 'variable':
    #     msg = f"With Variable constraints and fixed array size of {size_run_time_test[0][1]} "
    #     k_values, l_values = zip(*constraints) 
    #     constraints_size = [k * l for k,l in zip(k_values,l_values)]
    #     run_times = [run_time for run_time, _ in size_run_time_test]
    #     plt.figure(figsize=(8, 5))
    #     plt.plot(constraints_size, run_times, marker = 'o',color='blue', alpha=0.5)
    #     plt.title(f'Size vs. Run Time for {algorithm_name} {msg}')
    #     plt.xlabel('Constraints Size')
    #     plt.ylabel('Run Time (seconds)')
    #     plt.show()
    # else:
    #     msg = f"With fixed constraints (2,3)" if constraints_type == 'fixed' else ""
    #     sizes = [size for _, size in size_run_time_test]
    #     run_times = [run_time for run_time, _ in size_run_time_test]
    #     plt.figure(figsize=(8, 5))
    #     plt.plot(sizes, run_times, marker = 'o',color='blue', alpha=0.5)
    #     plt.title(f'Size vs. Run Time for {algorithm_name} {msg}')
    #     plt.xlabel('Matrix Size')
    #     plt.ylabel('Run Time (seconds)')
    #     plt.show()
    




    # ... Add more plots as needed ...






