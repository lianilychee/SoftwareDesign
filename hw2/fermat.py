'''
Liani Lye, HW 02
SoftDes Fall '14
Due 09.16.14
'''

a = int(raw_input("enter value for a: "));
b = int(raw_input("enter value for b: "));
c = int(raw_input("enter value for c: "));
n = int(raw_input("enter value for n: "));

def check_fermat():
	if (a**n + b**n) == c**n:
		print "Fermat's theorem holds."
	else:
		print "That doesn't work."

check_fermat()