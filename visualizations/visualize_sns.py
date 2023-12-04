import matplotlib.pyplot as plt
import seaborn as sns


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
    plt.figure(figsize=(10, 6))
    sns.barplot(x=labels, y=counts, palette=['#66c2a5', '#fc8d62', '#8da0cb'])
    for i, count in enumerate(counts):
        plt.text(i, count, str(count), ha='center', va='bottom', fontsize=12, fontweight='bold', color='black')
    plt.title(f'Test Results for {algorithm_name} {msg}', fontsize=16, fontweight='bold')
    plt.xlabel('Test Result', fontsize=14)
    plt.ylabel('Number of Test Cases', fontsize=14)
    plt.show()

    # Percentage Pie Chart
    labels = ['Successes', 'Failures']
    sizes = [test_results['successes'], test_results['failures']]
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#66ff66', '#ff6666'], startangle=90, explode=(0.1, 0))
    plt.title(f'Test Results Percentage for {algorithm_name} {msg}', fontsize=16, fontweight='bold')
    plt.legend(loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12)
    plt.show()

    # Line plot for Size vs. Run Time
    if constraints and constraints_type == 'variable':
        k_values, l_values = zip(*constraints)
        constraints_size = [k * l for k, l in zip(k_values, l_values)]
        run_times = [run_time for run_time, _ in size_run_time_test]
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=constraints_size, y=run_times, marker='o', color='#1f78b4', alpha=0.7, label='Run Time')
        # sns.scatterplot(x=constraints_size, y=run_times, color='#e31a1c', s=50, label='Data Points')
        plt.title(f'Size vs. Run Time for {algorithm_name} {msg}', fontsize=16, fontweight='bold')
        plt.xlabel('Constraints Size (k * l)', fontsize=14)
        plt.ylabel('Run Time (seconds)', fontsize=14)
        plt.legend(fontsize=12)
        plt.show()
    else:
        sizes = [size for _, size in size_run_time_test]
        run_times = [run_time for run_time, _ in size_run_time_test]
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=sizes, y=run_times, marker='o', color='#1f78b4', alpha=0.7, label='Run Time')
        # sns.scatterplot(x=sizes, y=run_times, color='#e31a1c', s=50, label='Data Points')
        plt.title(f'Size vs. Run Time for {algorithm_name} {msg}', fontsize=16, fontweight='bold')
        plt.xlabel('Matrix Size', fontsize=14)
        plt.ylabel('Run Time (seconds)', fontsize=14)
        plt.legend(fontsize=12)
        plt.show()

    # Histogram for Run Times
    plt.figure(figsize=(10, 6))
    sns.histplot([run_time for run_time, _ in size_run_time_test], bins=20, color='#1f78b4', edgecolor='black')
    plt.title(f'Distribution of Run Times for {algorithm_name} {msg}', fontsize=16, fontweight='bold')
    plt.xlabel('Run Time (seconds)', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.show()

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