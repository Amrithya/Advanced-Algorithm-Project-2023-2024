'''this is a helper function that will compute the sum of a subarray within a 2D matrix
 giving it the top lef and bottom right indices'''
 
def calculate_subarray_sum(matrix, top, left, bottom, right):
    subarray_sum = 0
    for i in range(top, bottom + 1): 
        for j in range(left, right + 1): 
            subarray_sum += matrix[i][j] 
    return subarray_sum



'''this is a helper function that will print the subarray within a 2D matrix'''
def print_submatrix(matrix, top, left, bottom, right):
        
    print('\nSubmatrix')
    for i in range(top, bottom +1):
        for j in range(left, right +1):
            print(matrix[i][j], end="\t")
        print()
    print()