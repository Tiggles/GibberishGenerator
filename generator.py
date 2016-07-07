#!/usr/bin/python
#Built using python version 2.7

import argparse
from random import *

DEFAULT_LENGTH = 10000

def argument_parse():	
	parser = argparse.ArgumentParser(description="The magic gibberish generator!")
	parser.add_argument('-f', '--wordfile', default="words.txt", 
		help="File containing the words used in gibberish generation")
	parser.add_argument('-l','--limit', default=DEFAULT_LENGTH, type=int,
		help="Set the generation limit")
	return parser.parse_args()

def read_file(filename):
	return [ line.rstrip() for line in open(filename, 'r') ]

def generate_gib(words, is_capital, limit):
	capital = is_capital

	for i in range(0, limit):
		if capital:
			print words[randint(0, len(words)) - 1].title(),
			capital = False
		else:
			print words[randint(0, len(words)) - 1],

		if (randint(0, 1000) > 999):
			print '\b.\n'
			capital = True

		elif (randint(0, 1000) > 800):
			print "\b.",
			capital = True

if __name__ == "__main__":
	args = argument_parse()
	generate_gib( read_file( args.wordfile ), True, abs( args.limit ) )