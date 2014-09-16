n = int(raw_input("enter some integer n: "))

def factorial(n):
	for i in range(0, 5):
		result = n*(n-1)
		n = n - 1
		i = i+1
		print result

factorial(n)