import unittest
import time
from test_samples.samples import tests
from brute.helpers import print_submatrix

class TestAlgorithm(unittest.TestCase):
    def run_algorithm_tests(self, algorithm, algorithm_name):
        successful_tests = 0
        total_tests = len(tests)

        for i, test_sample in enumerate(tests):
            matrix = test_sample["matrix"]
            expected_result = test_sample["expected_result"]
            expected_indices = test_sample["subarray_indices"]
            # algorithm_args = test_sample.get("algorithm_args", ())

            with self.subTest(test_number=i + 1):
                start_time = time.time()  # Record the start time
                result, top_left, bottom_right = algorithm(matrix)
                end_time = time.time()  # Record the end time

                self.assertEqual(result, expected_result)
                self.assertTupleEqual(top_left, expected_indices[0])
                self.assertTupleEqual(bottom_right, expected_indices[1])

                # Print information for each test case
                print(f"\nTest Case {i + 1}:")
                print(f"Result: {result}")
                print(f"Expected Result: {expected_result}")
                print(f"Indices: {top_left} to {bottom_right}")
                print(f"Expected Indices: {expected_indices[0]} to {expected_indices[1]}")
                print(f"Matrix:")
                # print the matrix used
                for row in matrix:
                    print(row)
                print(f"Submatrix:")
                print_submatrix(matrix, top_left[0], top_left[1], bottom_right[0], bottom_right[1])

                # Increment the counter if the test passes
                successful_tests += 1

                # Print the time taken for the current test
                print(f"Time taken: {end_time - start_time:.6f} seconds\n")

        success_percentage = (successful_tests / total_tests) * 100
        print(f"Success Percentage for {algorithm_name}: {success_percentage:.2f}%")

if __name__ == '__main__':
    unittest.main()
