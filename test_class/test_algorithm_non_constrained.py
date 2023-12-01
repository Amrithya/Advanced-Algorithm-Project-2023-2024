import unittest
import timeit
from test_samples.test_non_constraint import tests
from brute.helpers import print_submatrix,calculate_subarray_sum

class TestAlgorithm(unittest.TestCase):
    """HELPER FUNCTIONS"""
    # check if its non rectangular
    def is_non_rectangular(self,matrix):
        return any(len(row) != len(matrix[0]) for row in matrix)
    
    # check if its a one dimensional matrix
    def is_one_dimensional(self, matrix):
        return isinstance(matrix, list) and all(isinstance(row, (int, float)) for row in matrix)
    
    # Check if the matrix is empty
    def is_empty(self, matrix):
        if not matrix:
            return True
    # Check if the matrix is all numerical values
    def has_non_numeric_values(self,matrix):
        return any(not isinstance(element, (int, float)) for row in matrix for element in row)
    

    def print_success_inofrmation(self,i,result,expected_result,top_left,bottom_right,expected_indices,matrix):
        print(f"\nTest Case {i + 1} \033[92msucceeded\033[0m")
        print(f"Result: {result}")
        print(f"Expected Result: {expected_result}")
        print(f"Indices: {top_left} to {bottom_right}")
        print(f"Expected Indices: {expected_indices[0]} to {expected_indices[1]}")
        print(f"Matrix:")
        # print the matrix used
        for row in matrix:
            print(row)
        #  print the submatrix answer
        print_submatrix(matrix, top_left[0], top_left[1], bottom_right[0], bottom_right[1])


    """RUNNING AN ALGORITHM AGAINST ALL CASES
    
    this is the test function that takes two inputs (algorithm_funciton, algorithm_name)
    - it prints all the test cases, the success rate
    - it returns a size_time list which is a list of tuples containing (running time for each run, elements in the matrix)
    - it returns number of successful runs
    - it returns number of failed runs
    
    """  
    
                    
    def run_algorithm_tests(self, algorithm, algorithm_name):
        print(f"\nTESTING {algorithm_name} \n\n================================")
        successful_tests = 0
        total_tests = len(tests)
        skipped_tests = 0 # counts invalid tests
        failed_tests = 0 # counts failed tests
        size_run_time_test = []
        for i, test_sample in enumerate(tests):
            matrix = test_sample["matrix"]
            
            if not isinstance(matrix,list):
                print(f"\nTest Case {i + 1} skipped: Input not a matrix.")
                skipped_tests += 1
                continue
            # if empty matrix
            if self.is_empty(matrix):
                print(f"\nTest Case {i + 1} skipped: Matrix is empty.")
                skipped_tests += 1
                continue
            
            # if one dimensional matrix
            if self.is_one_dimensional(matrix):
                print(f"\nTest Case {i + 1} skipped: Matrix is one-dimensional.")
                skipped_tests += 1
                continue
            
            # if non rectangular matrix
            if self.is_non_rectangular(matrix):
                print(f"\nTest Case {i + 1} skipped: Matrix is non-rectangular.")
                skipped_tests += 1
                continue
            # if it has non numeric values
            if self.has_non_numeric_values(matrix):
                print(f"\nTest Case {i + 1} skipped: Matrix contains non-numeric values.")
                skipped_tests += 1
                continue
            
            rows = len(matrix)
            columns = len(matrix[0])
            n_elements = rows * columns
            expected_result = test_sample["expected_result"]
            expected_indices = test_sample["subarray_indices"]
          
            

            with self.subTest(test_number=i + 1):
                try:
                    # calculate the time for the algorithm
                    start_time = timeit.default_timer()  # Record the start time
                    result, top_left, bottom_right = algorithm(matrix)
                    end_time = timeit.default_timer()  # Record the end time
                    
                    self.assertEqual(result, expected_result)
                    
                    self.assertTupleEqual(top_left, expected_indices[0])
                    self.assertTupleEqual(bottom_right, expected_indices[1])

                    self.print_success_inofrmation(i,result,expected_result,top_left,bottom_right,expected_indices,matrix)
                    successful_tests += 1
                    execution_time = end_time - start_time
                    size_run_time_test.append((execution_time,n_elements))
                    # Print the time taken for the current test
                    print(f"Time taken: {execution_time:.6f} seconds\n")

                except AssertionError as e:
                    ## check if the error was raised because It found a differnet solution not because it failed
                    if result == expected_result:
                        print("\033[36mAlgorithm Found a different solution than the expected solution but it is the right solution\033[0m")
                        self.print_success_inofrmation(i,result,expected_result,top_left,bottom_right,expected_indices,matrix)
                        execution_time = end_time - start_time
                        size_run_time_test.append((execution_time,n_elements))
                        successful_tests += 1
                        print(f"Time taken: {execution_time:.6f} seconds\n")
                        continue

                    print(f"\nTest Case {i + 1} \033[91mfailed\033[0m: {e}")
                    print(f"Result: {result}")
                    print(f"Expected Result: {expected_result}")
                    print(f"Indices: {top_left} to {bottom_right}")
                    print(f"Expected Indices: {expected_indices[0]} to {expected_indices[1]}")
                    print(f"Matrix:")
                    for row in matrix:
                        print(row)
                    # # print the submatrix answer
                    print(f"Submatrix:")
                    print_submatrix(matrix, top_left[0], top_left[1], bottom_right[0], bottom_right[1])
                    # increment the counter if the test fails
                    failed_tests+=1
                    continue

        success_percentage = (successful_tests / (total_tests-skipped_tests)) * 100
        print(f"\033[92mSuccess Percentage for {algorithm_name}: {success_percentage:.2f}%\033[0m")
        print(f"\033[92m{successful_tests} Successes\033[0m, \033[91m{failed_tests} Fails\033[0m, \033[93m{skipped_tests} Skipped invalid tests\033[0m")
        # calculate the average time 
        
        return size_run_time_test,successful_tests,failed_tests

if __name__ == '__main__':
    unittest.main()
