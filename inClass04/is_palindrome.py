import difflib

actual = str(raw_input("type something: "))

def is_palindrome():
	reverse = actual[::-1]
	if reverse == actual:
		print "hooray"
	else:
		print "no go"

is_palindrome()