from random import *

capital = True

fin = open('words.txt', 'r')
words = []
for line in fin:
	words.append(line.rstrip())

for i in range(0, 250 * 40):
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
