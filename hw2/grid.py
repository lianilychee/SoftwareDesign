'''
Liani Lye, HW 02
SoftDes Fall '14
Due 09.16.14
'''

n = raw_input("enter grid dimension: ");
n = int(n);
horiz = "+ - - - - ";
vert = "|         ";

fullHoriz = horiz*n + "+";
fullVert = ((vert*n + "|") + "\n")*3 + (vert*n + "|");

# forget about ending the rows / column for now

def createGrid():
	for i in range(0, n):
		print fullHoriz;
		print fullVert;
	print fullHoriz;
	
createGrid();