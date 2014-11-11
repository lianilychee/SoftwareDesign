x = int(raw_input("enter some integer x: "))
y = int(raw_input("enter some integer y: "))

def sum_int():
	setRange = abs(x-y) + 1
	bounds = x+y
	sum = bounds * setRange/2
	print sum

sum_int()