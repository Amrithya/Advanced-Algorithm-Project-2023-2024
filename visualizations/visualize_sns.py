import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

def create_test_result_plots(test_results, algorithm_name):
    constraints = test_results['constraints']
    constraints_type = test_results['constraints_type']
    size_run_time_test = test_results['size_run_time_test']

    msg = ""
    if constraints and constraints_type == 'variable':
        msg = f"With Variable constraints and fixed array size of {size_run_time_test[0][1]}"
    else:
        msg = f"With fixed constraints ({constraints[0][0]},{constraints[0][1]})" if constraints_type == 'fixed' else ""

    # Set seaborn style and context
    sns.set_style("whitegrid")
    sns.set_context("talk")

    # Bar Chart for Successes, Failures, and Skipped
    labels = ['Successes', 'Failures', 'Skipped']
    counts = [test_results['successes'], test_results['failures'], test_results['skipped']]
    colors = ['#28a745', '#dc3545', '#ffc107']  # Green, Red, Yellow

    plt.figure(figsize=(10, 6))
    sns.barplot(y=labels, x=counts, palette=colors, orient='h')

    plt.title(f'Test Results for {algorithm_name} {msg}', fontsize=18, fontweight='bold')
    plt.ylabel('Test Result', fontsize=16)
    plt.xlabel('Number of Test Cases', fontsize=16)

    # Adding custom data labels
    for index, value in enumerate(counts):
        plt.text(value, index, f' {value}', color='black', fontweight='bold', va='center')

    # Setting a stylish background
    sns.set_style("whitegrid")

    # Adding grid lines for better readability
    plt.grid(axis='x', linestyle='--')

    plt.show()



    # Improved Percentage Donut Chart
    labels = ['Successes', 'Failures']
    sizes = [test_results['successes'], test_results['failures']]
    colors = ['#28a745', '#dc3545']  # Green for Successes, Red for Failures

    plt.figure(figsize=(8, 8))
    # Creating a donut chart
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, wedgeprops=dict(width=0.3), explode=(0.1, 0))

    plt.title(f'Test Results Percentage for {algorithm_name} {msg}', fontsize=18, fontweight='bold')

    # Adding a central label
    total = sum(sizes)
    plt.text(0, 0, f'Total\n{total}', ha='center', va='center', fontsize=14, color='black', fontweight='bold')

    # Improved legend positioning and styling
    plt.legend(loc="best", fontsize=12, title='Test Results', title_fontsize='13', bbox_to_anchor=(1, 0.5))

    plt.show()


    # Function to calculate trend line
    def calculate_trend_line(x, y):
        z = np.polyfit(x, y, 1)  # Fit a first degree polynomial (linear)
        p = np.poly1d(z)  # Return the polynomial function
        return p, z

    # Function to plot Size vs. Run Time
    def plot_size_vs_run_time(sizes, run_times, xlabel):
        plt.figure(figsize=(10, 6))
        base_color = '#1f78b4'  # Base color

        # Creating a line plot
        sns.lineplot(x=sizes, y=run_times, marker='o', color=base_color, alpha=0.7, label='Run Time')

        # Calculating and adding trend line
        trend_line, coeffs = calculate_trend_line(sizes, run_times)
        plt.plot(sizes, trend_line(sizes), linestyle="--", color='darkblue', label='Trend Line')

        # Displaying the equation of the trend line
        equation_text = f'y = {coeffs[0]:.2f}x + {coeffs[1]:.2f}'
        plt.text(sizes[-1], trend_line(sizes)[-1], equation_text, fontsize=12, color='darkblue', verticalalignment='bottom')

        plt.title(f'Size vs. Run Time for {algorithm_name} {msg}', fontsize=16, fontweight='bold')
        plt.xlabel(xlabel, fontsize=14)
        plt.ylabel('Run Time (seconds)', fontsize=14)
        plt.legend(fontsize=12)
        plt.show()

    # Example usage
    if constraints and constraints_type == 'variable':
        k_values, l_values = zip(*constraints)
        constraints_size = [k * l for k, l in zip(k_values, l_values)]
        run_times = [run_time for run_time, _ in size_run_time_test]
        plot_size_vs_run_time(constraints_size, run_times, 'Constraints Size (k * l)')
    else:
        sizes = [size for _, size in size_run_time_test]
        run_times = [run_time for run_time, _ in size_run_time_test]
        plot_size_vs_run_time(sizes, run_times, 'Matrix Size')


    # # Box Plot for Run Times
    # plt.figure(figsize=(10, 6))
    # sns.boxplot(x=[run_time for run_time, _ in size_run_time_test], orient='h', width=0.7, palette='pastel')
    # plt.title(f'Box Plot of Run Times for {algorithm_name} {msg}', fontsize=16, fontweight='bold')
    # plt.xlabel('Run Time (seconds)', fontsize=14)
    # plt.yticks([])
    # plt.show()

    # # Violin Plot for Run Times
    # plt.figure(figsize=(10, 6))
    # sns.violinplot(x=[run_time for run_time, _ in size_run_time_test], color='#1f78b4')
    # plt.title(f'Violin Plot of Run Times for {algorithm_name} {msg}', fontsize=16, fontweight='bold')
    # plt.xlabel('Run Time (seconds)', fontsize=14)
    # plt.show()

    # # Pair Plot for Run Times and Constraints Size (if applicable)
    # if constraints and constraints_type == 'variable':
    #     data = {'Constraints Size': constraints_size, 'Run Time': run_times}
    #     df = pd.DataFrame(data)
    #     plt.figure(figsize=(12, 8))
    #     sns.pairplot(df, markers='o', palette='husl', height=4, diag_kind='kde')
    #     plt.suptitle(f'Pair Plot: Constraints Size vs. Run Time for {algorithm_name} {msg}', y=1.02, fontsize=16, fontweight='bold')
    #     plt.show()

    return