import math 

def approximate_e():
	decimals = int(raw_input("enter the number of decimal places you want: "))
	strE = str(math.e) 
	print strE[:decimals+2]

approximate_e()