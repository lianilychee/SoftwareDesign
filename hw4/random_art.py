# -*- coding: utf-8 -*-
"""
Random_art.py
@author: lianilye, adapted from amonmillner's work (originally pruvolo)
"""

# you do not have to use these particular modules, but they may help
from random import randint
import math
from PIL import Image
import time
import datetime

# min_depth = int(raw_input("min_depth: "))   # min amt of nesting
# max_depth = int(raw_input("max_depth: "))   # max amt of nesting
# a = int(raw_input("a: "))   # 1st input for build_random_function()
# b = int(raw_input("b: "))   # 2nd input for build_random_function()

time = str(datetime.datetime.now())
timeClipped = time[0:19]

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
	

	
if __name__ == '__main__':
	
	img = Image.new('RGB', (350, 350))
	pixels = img.load() # create the pixel map
	
	# generates random function for each color channel

	funcR = build_rand_func(6,15) 
	print "funcR" + str(funcR) + "\n"
	funcG = build_rand_func(9,11)
	print "funcG" + str(funcG) + "\n"
	funcB = build_rand_func(5,12)
	print "funcB" + str(funcB) + "\n"

	for i in range(img.size[0]):    # for every pixel:
		for j in range(img.size[1]):
			posX = remap_interval(i, 0, 350, -1,1) #scales rand func inputs to [-1,1]
			posY = remap_interval(j, 0, 350, -1, 1)
			rawR = eval_rand_func(funcR, posX, posY) #eval rand func
			rawG = eval_rand_func(funcG, posX, posY)
			rawB = eval_rand_func(funcB, posX, posY)
			filterR = int(remap_interval(rawR, -1, 1, 0, 255))  #scale output to [0, 250]
			filterG = int(remap_interval(rawG, -1, 1, 0, 255))
			filterB = int(remap_interval(rawB, -1, 1, 0, 255))
			pixels[i,j] = (filterR, filterG, filterB ) # set the color accordingly
	
	img.save(timeClipped + ".jpg")