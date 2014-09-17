def is_prime():
	n = int(raw_input("enter some integer n: "))

	if n == 2:
		print "number is prime"

	# if n != 2 and n%2 == 0:
	# 	print "number is even"

	# if n%2 != 0:

	for x in range (3, n):
		if n%x == 0:
			print "number is not prime"
			break
		else:
			print "number is prime"
			break


is_prime()