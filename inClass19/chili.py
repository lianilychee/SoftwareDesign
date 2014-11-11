# -*- coding: utf-8 -*-
class Meal(object):
	def __init__(self):
		pass

	def taste(self):
		print "A tasty meal"


class Soup(Meal):
	def taste(self):
		print "A soup that's also a "
		super(Soup, self).taste()

def main():
	m = Meal()
	s = Soup()
	m.taste()
	s.taste()

if __name__=="__main__":
	main()