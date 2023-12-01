from brute.brute_force import max_subarray_2d_polynomial, max_subarray_2d_polynomial_constrained
from test_algorithm import TestAlgorithm

test_algorithm_instance = TestAlgorithm()

# Test unconstrained algorithm

test_algorithm_instance.run_algorithm_tests(max_subarray_2d_polynomial, "Brute Force non Constrained algorithm")

