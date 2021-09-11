# your code goes here
t = int(input())

def find_quarrrel(n,test_input, total_sum, min_, i):
	
	if(i < n):
		print(i, n, min_)
		if total_sum == 0:
			return 0
		if(total_sum <=min_ and total_sum != 0):
			min_ = total_sum
		find_quarrrel(n, test_input, total_sum-test_input[i][0], min_, i+1)
		find_quarrrel(n, test_input, total_sum-test_input[i][1], min_, i+1)
	else:
		return min_


for i in range(t):
	n = int(input())
	test_input = [[0]*2 for i in range(n)]
	total_sum = 0
	for i in range(n):
		test_input[i][0], test_input[i][1] = [int(item) for item in input().split()]
		total_sum += test_input[i][0] + test_input[i][1]

	dict_members = {}
	
	min_= find_quarrrel(n, test_input, total_sum, float('inf'), 0)

	print(min_)
	

	
				
			
	