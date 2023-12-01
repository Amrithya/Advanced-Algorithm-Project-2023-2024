from brute.brute_force import brute_force_non_constrained, brute_force_constrained
from greedy.greedy_algorithm import greedy_algorithm_constrained,greedy_algorithm_non_constrained
from test_algorithm import TestAlgorithm
import numpy as np
import timeit

test_algorithm_instance = TestAlgorithm()

# Test unconstrained algorithm
size_time, success, fail = test_algorithm_instance.run_algorithm_tests(brute_force_non_constrained, "Brute Force non Constrained algorithm")
# print(size_time)
# print(success)
# print(fail)
start_time = timeit.default_timer()  # Record the start time
result, top_left, bottom_right = greedy_algorithm_non_constrained(np.random.randint(-50,50,(1000,1000)))
end_time = timeit.default_timer()  # Record the end time
execution_time = end_time-start_time
print(result, top_left, bottom_right, execution_time)



# test_algorithm_instance.run_algorithm_tests(greedy_algorithm_non_constrained, "Greedy_algorithm_non_constrained")


