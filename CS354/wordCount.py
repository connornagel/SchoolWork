#!/usr/bin/python
import sys

wordCollection = {}
for line in sys.stdin:
	
	line = line.strip(',.:;\'\"&!?-_')

	words = line.split()

	for word in words:
		currentWord = word.lower().strip(',.:;\'\"&!?-_')
		if currentWord in wordCollection:
			wordCollection[currentWord] += 1
		else:
			wordCollection[currentWord] = 1
		
		
for currentWord in wordCollection:
	print ("%s : %s" % (currentWord, wordCollection[currentWord]))


