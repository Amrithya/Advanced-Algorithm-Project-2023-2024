# Advanced-Algorithm-Project-2023-2024
This repository is dedicated to solving the Matrix Maximum Segment Problem in a 2-dimensional scenario, commonly known as the Maximum Subarray Problem. Our primary objective is to implement various algorithms for this task and provide a comprehensive experimental analysis of their runtime performance and the quality of results. Explore this repository to access the code, documentation, and data related to our research and implementations.

# Dynamic programming 

Algorithm :

1. Get the number of rows and column of the input matrix and set it to ROW and COL respectively.
2. Initialize 
	maxSum = -999999999999 	
	start_i, start_j, end_i, end_j = null
	i,j,k = null
	temp[] = [null] * ROW
	sum = 0 
	top = [0]
	bottom = [0]
3. Loop i to COL
	Initialize temp = [0] * ROW
	loop j from i to COL
		loop k to ROW
			temp[j] = Input_Matrix[k][j]
		sum = indices(temp,top,bottom,ROW)
		if sum > maxSum
			set sum as maxSum
			start_i = i
			start_j = j
			end_i = top[0]
			end_j = bottom[0]
4. in indices(temp,top,bottom,ROW)
	Initialize 
	  sum = 0, maxSum = -999999999999, i = 0 
	bottom[0] = -1
	start = 0
	loop i to ROW
		sum += temp[i]
		if sum < 0, set sum = 0 and start = i + 1
		else if sum > maxSum,
			set maxSum = sum, top[0] = start,bottom[0] = i
	if bottom[0] != -1, return maxSum
	maxSum = temp[0]
	top[0] = bottom[0] = 0
	loop i from 1 to ROW
		if temp[i] > maxSum, set maxSum = temp[i]
		and top[0] = bottom[0] = i
	return maxSum
5. Print start_i, start_j, end_i, end_j
				
