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


def build_rand_func(min_depth, max_depth):
	""" Takes inputs recursion parameters min_depth, max_depth to generate random function.
	"""

	options = [['prod'],['sin_pi'],['cos_pi'],['A'],['B']]

	# base case
	if max_depth == 1:
		return ['A']

	# if min_depth reached, also choose base case
	elif min_depth <= 1:

		func_choice = options[randint(0,4)] # choose random func

		# allows products to take two imputs
		if func_choice == ['prod']:
			return func_choice + [build_rand_func(min_depth-1, max_depth-1), build_rand_func(min_depth, max_depth)]

		# if base case reached, end recursion
		elif func_choice == ['A'] or func_choice == ['B']:
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

def eval_rand_func(f, a, b):
	""" Pass in a list of strings that represent functions and solve in terms of inputted vals a and b
	"""

	if f[0] == 'prod':
		return eval_rand_func(f[1], a, b) * eval_rand_func(f[2], a, b)

	elif f[0] == 'cos_pi':
		return math.cos(math.pi * eval_rand_func(f[1], a, b))

	elif f[0] == 'sin_pi':
		return math.sin(math.pi * eval_rand_func(f[1], a, b))

	elif f[0] == 'A':
		return a
		
	else:
		return b  

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
	""" Maps the input value that is in the interval [input_interval_start, input_interval_end]
		to the output interval [output_interval_start, output_interval_end].  The mapping
		is an affine one (i.e. output = input*c + b).
	"""

	# shift the zero
	zero = (output_interval_start - input_interval_start)
	
	# stretch/compress after shifting
	change_factor = float(output_interval_end)/ (input_interval_end + zero)

	# apply stretching/compression
	new_value = (val+zero)*change_factor

	return new_value
	
	