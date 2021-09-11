# your code goes here
t = int(input())

def is_prime(n):
	if(n < 2):
		return False
	if(n==2 or n==3):
		return True
	for i in range(2, n//2+1):
		# print('check_prime', i, n)
		if n%i==0:
			return False
	return True



for i in range(t):
	n = int(input())
	j = 1
	count_res = 0
	for i in range(1, n+1):
		res = is_prime(i)
		if (res):
			while((n % (i*j))==0 and j<=n//2+1):
				print(i, j, n)
				count_res += 1
				n = n//2
				j += 1
	print(count_res)
				
			
	