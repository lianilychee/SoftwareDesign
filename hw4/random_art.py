# -*- coding: utf-8 -*-
"""
Random_art.py
@author: lianilye, adapted from amonmillner's work (originally pruvolo)
"""

# you do not have to use these particular modules, but they may help
from random import randint
import math
import Image

# min_depth = int(raw_input("min_depth: "))   # min amt of nesting
# max_depth = int(raw_input("max_depth: "))   # max amt of nesting
# a = int(raw_input("a: "))   # 1st input for build_random_function()
# b = int(raw_input("b: "))   # 2nd input for build_random_function()


def build_random_function(min_depth, max_depth):
	"""
	Takes inputs recursion parameters min_depth, max_depth to generate random function.
	"""

	options = [['prod'],['sin_pi'],['cos_pi'],['a'],['b']]

	# base case
	if max_depth == 1:
		return ['a']

	# if min_depth reached, also choose base case
	elif min_depth <= 1:

		func_choice = options[randint(0,4)] # choose random func

		# allows products to take two imputs
		if function_choice == ['prod']:
			return func_choice + [build_rand_func(min_depth-1, max_depth-1), build_rand_func(min_depth, max_depth)]

		# if base case reached, end recursion
		elif func_choice == ['a'] or func_choice == ['b']:
			return func_choice

		# otherwise, recurse as usual (single input)
		else:
			return func_choice + [build_rand_func(min_depth-1, max_depth-1)]

	# if min_depth or max_depth not reached, loop again with min/max counters decremented
	else:
		func_choice = options[randint(0, 2)]

		# allows products to take two inputs
		if func_choice != ['prod']:
			return func_choice + [(build_rand_func(min_depth-1, max_depth-1))]

		# otherwise, recurse as usual
		else:
			return func_choice + [build_rand_func(min_depth-1, max_depth-1), build_rand_func(min_depth-1, max_depth-1)]

	# print rand_func
	# return rand_func

def evaluate_random_function(f, x, y):
	""" your doc string goes here
	"""

	# your code goes here

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
	""" Maps the input value that is in the interval [input_interval_start, input_interval_end]
		to the output interval [output_interval_start, output_interval_end].  The mapping
		is an affine one (i.e. output = input*c + b).
	
		TODO: please fill out the rest of this docstring
	"""
	# your code goes here
	


#your additional code and functions go here
