import unittest
import timeit
from test_samples.test_non_constraint import non_constrained_tests as non_constrained_tests
from test_samples.test_constraint_variable_K_L import constrained_tests_variable_K_L as constrained_tests_variable_K_L 
from test_samples.test_constraint_fixed_K_L import constrained_tests_fixed_K_L as constrained_tests_fixed_K_L 

from brute.helpers import print_submatrix, calculate_subarray_sum


class TestAlgorithm(unittest.TestCase):
    """HELPER FUNCTIONS"""

    def is_valid_matrix(self, matrix):
        """
        Check if a matrix is valid based on certain criteria.

        Parameters:
        - matrix: The input matrix to be checked.

        Returns:
        - True if the matrix is valid, False otherwise.
        - A string describing the reason for invalidity if applicable.
        """

        # Check if the matrix is empty
        if not matrix:
            return False, "Matrix is empty."

        # Check if the matrix is one-dimensional
        if isinstance(matrix, list) and any(isinstance(row, (int, float)) for row in matrix):
            return False, "Matrix is one-dimensional."

        # Check if the matrix is non-rectangular
        if any(len(row) != len(matrix[0]) for row in matrix):
            return False, "Matrix is non-rectangular."

        # Check if the matrix contains non-numeric values
        if any(not isinstance(element, (int, float)) for row in matrix for element in row):
            return False, "Matrix contains non-numeric values."

        # If all checks pass, the matrix is valid
        return True, "Matrix is valid."

    def print_success_information(self, i, result, expected_result, top_left, bottom_right, expected_indices, matrix):
        """
        Print information about a successful test case.

        Parameters:
        - i: Test case number.
        - result: Result from the algorithm.
        - expected_result: Expected result for the test case.
        - top_left: Top-left indices of the submatrix.
        - bottom_right: Bottom-right indices of the submatrix.
        - expected_indices: Expected indices of the submatrix.
        - matrix: The input matrix.
        """
        print(f"\nTest Case {i + 1} \033[92msucceeded\033[0m")
        print(f"Result: {result}")
        print(f"Expected Result: {expected_result}")
        print(f"Indices: {top_left} to {bottom_right}")
        print(f"Expected Indices: {expected_indices[0]} to {expected_indices[1]}")
        print(f"Matrix:")
        # Print the matrix used
        for row in matrix:
            print(row)
        # Print the submatrix answer
        print_submatrix(matrix, top_left[0], top_left[1], bottom_right[0], bottom_right[1])

    """RUNNING AN ALGORITHM AGAINST ALL CASES
    
    The class includes a method named run_algorithm_tests(algorithm, algorithm_name, constrained_type=None),
    which executes the algorithm against a set of predefined test cases. The method takes three parameters:

        - algorithm: The algorithm to be tested.
        - algorithm_name: A string representing the name of the algorithm.
        - constrained_type: A string indicating the type of constraints for the test cases 
        (either "variable," "fixed," or None for unconstrained tests).
    
    Test Results:
       - The method executes the algorithm against each test case, providing detailed information for each test,
       - including success, failure, or skipped status. It prints information such as the test number, result,
       - expected result, indices, matrix, and submatrix.

    The method returns a dictionary named test_results, which includes the following key-value pairs:

        - size_run_time_test: A list of tuples containing the execution time and the number of elements for each test case.
        - successes: The number of successful test cases.
        - failures: The number of failed test cases.
        - skipped: The number of skipped test cases due to invalid input matrices.
        - success_percentage: The percentage of successful test cases out of the total valid test cases.
        - constraints: A list of tuples containing the constraints for each test case (k,l) or empty list if no constraints
    """  
    
                    
    def run_algorithm_tests(self, algorithm, algorithm_name, constrained_type=None):
        # Check which type of constraint is used for testing 
        if constrained_type == "variable":
            tests = constrained_tests_variable_K_L
            test_type = "WITH VARIABLE CONSTRAINTS"
        elif constrained_type == "fixed":
            tests = constrained_tests_fixed_K_L
            test_type = "WITH FIXED CONSTRAINTS"
        else:
            tests = non_constrained_tests
            test_type = "WITHOUT CONSTRAINTS"

        print(f"\nTESTING {algorithm_name} {test_type}\n\n================================")
        
        # Declare variables needed for tests
        successful_tests = 0
        total_tests = len(tests)
        skipped_tests = 0  # Counts invalid tests
        failed_tests = 0 
        size_run_time_test = []  # List of tuples containing (test_time, array_size)
        constraints = [] # List of tuples containing (k, l)
        # Loop over all tests
        for test_number, test_sample in enumerate(tests):
            matrix = test_sample["matrix"]
            
            # Check if matrix is valid before running tests (validation)
            is_valid, reason = self.is_valid_matrix(matrix)
            if not is_valid:
                print(f"\nTest Case {test_number + 1} skipped: {reason}")
                skipped_tests += 1
                continue
            
            # Get the expected results from the test and some information about the matrix
            rows = len(matrix)
            columns = len(matrix[0])
            n_elements = rows * columns
            expected_result = test_sample["expected_result"]
            expected_indices = test_sample["subarray_indices"]
          
            
            # Start testing 
            with self.subTest(test_number=test_number + 1):
                try:
                    # Calculate the time for the algorithm
                    start_time = timeit.default_timer()  # Record the start time
                    
                    # Check the constraint type and if it is constrained, validate that k and l are less than the size of the rows and columns
                    if constrained_type == "variable" or constrained_type == "fixed":
                        k, l = test_sample["constraints"]
                        
                        if k > rows or l > columns:
                            print(f"\nTest Case {test_number + 1} skipped: Constraints k or l exceed matrix dimensions.")
                            skipped_tests += 1
                            continue
                        
                        result, top_left, bottom_right = algorithm(matrix, k, l)
                    else:
                        result, top_left, bottom_right = algorithm(matrix)
                    end_time = timeit.default_timer()  # Record the end time
                    
                    # Asserting test results against expected results
                    self.assertEqual(result, expected_result)
                    self.assertTupleEqual(top_left, expected_indices[0])
                    self.assertTupleEqual(bottom_right, expected_indices[1])

                    # Printing information about test success
                    self.print_success_information(test_number, result, expected_result, top_left, bottom_right, expected_indices, matrix)
                    successful_tests += 1
                    execution_time = end_time - start_time
                    size_run_time_test.append((execution_time, n_elements))
                    if constrained_type == "variable" or constrained_type == "fixed":
                        constraints.append((k,l))
                    # Print the time taken for the current test
                    print(f"Time taken: {execution_time:.6f} seconds\n")

                except AssertionError as e:
                    ## Check if the error was raised because it found a different solution, not because it failed
                    if result == expected_result:
                        print("\033[36mAlgorithm Found a different solution than the expected solution but it is the right solution\033[0m")
                        self.print_success_information(test_number, result, expected_result, top_left, bottom_right, expected_indices, matrix)
                        execution_time = end_time - start_time
                        size_run_time_test.append((execution_time, n_elements))
                        successful_tests += 1
                        print(f"Time taken: {execution_time:.6f} seconds\n")
                        if constrained_type == "variable" or constrained_type == "fixed":
                            constraints.append((k,l))
                        continue

                    print(f"\nTest Case {test_number + 1} \033[91mfailed\033[0m: {e}")
                    print(f"Result: {result}")
                    print(f"Expected Result: {expected_result}")
                    print(f"Indices: {top_left} to {bottom_right}")
                    print(f"Expected Indices: {expected_indices[0]} to {expected_indices[1]}")
                    print(f"Matrix:")
                    for row in matrix:
                        print(row)
                    # Print the submatrix answer
                    print(f"Submatrix:")
                    print_submatrix(matrix, top_left[0], top_left[1], bottom_right[0], bottom_right[1])
                    # Increment the counter if the test fails
                    failed_tests += 1
                    continue

        success_percentage = (successful_tests / (total_tests - skipped_tests)) * 100
        print(f"\033[92mSuccess Percentage for {algorithm_name}: {success_percentage:.2f}%\033[0m")
        print(f"\033[92m{successful_tests} Successes\033[0m, \033[91m{failed_tests} Fails\033[0m, \033[93m{skipped_tests} Skipped invalid tests\033[0m")
        test_results = {'size_run_time_test': size_run_time_test,
                        'successes': successful_tests, 
                        'failures': failed_tests,
                        'skipped': skipped_tests,
                        'success_percentage': success_percentage,
                        'constraints': constraints,
                        'constraints_type': constrained_type if constraints else None}
        return test_results

if __name__ == '__main__':
    unittest.main()
