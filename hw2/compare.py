'''
Liani Lye, HW 02
SoftDes Fall '14
Due 09.16.14

Write a compare function that returns 1 if x > y, 0 if x == y, and -1 if x < y
'''

x = int(raw_input("enter value for x: "));
y = int(raw_input("enter value for y: "));

def compare():
	if x > y:
		return 1;
	if x == y:
		return 0;
	if x < y:
		return -1;

print compare();