#!/usr/bin/env python3
#Built using python version 3!

import argparse
from random import *

DEFAULT_LENGTH = 10000

def argument_parse():	
	parser = argparse.ArgumentParser(description="The magic gibberish generator!")
	parser.add_argument('-f', '--wordfile', default="words.txt", 
		help="File containing the words used in gibberish generation")
	parser.add_argument('-l','--limit', default=DEFAULT_LENGTH, type=int,
		help="Set the generation limit")
	parser.add_argument('-p','--paragraph', default=1, type=int, 
		help="Set the paragraph random intensity on a scale from 0-1000. A value of 1000 splits each word into a paragraph, while a value of 0 does not create any paragraphs")
	parser.add_argument('-s','--sentences', default=200, type=int, 
		help="Set the sentence random intensity on a scale from 0-1000. A value of 1000: Every word is an sentence; A value of 0: No sentences")
	return parser.parse_args()

def read_file(filename):
	with open(filename, 'r') as filein:
		return tuple( line.rstrip() for line in filein )

def generate_gib(words, limit, plimit, slimit):
	capital = True

	for i in range(0, limit):
		if capital:
			print(words[randint(0, len(words)) - 1].title(), end="")
			capital = False
		else:
			print(words[randint(0, len(words)) - 1], end="")

		if (randint(0, 1000) > abs(1000 - plimit)):
			print('\b.\n')
			capital = True
		elif (randint(0, 1000) > abs(1000 - slimit)):
			print("\b.", end="")
			capital = True
	print("\b.\n")

if __name__ == "__main__":
	args = argument_parse()
	generate_gib( read_file( args.wordfile ), abs( args.limit ), 
		abs( args.paragraph ), abs( args.sentences ) )
