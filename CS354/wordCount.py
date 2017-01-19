#!/usr/bin/python
import sys

"""@Author Connor Nagel
	WordCounter
"""
wordCollection = {}

#Splits and strips down each input line into words that are stored in wordCollection

for line in sys.stdin:
	
	line = line.strip(',.:;\'\"&!?-_')

	words = line.split()

#Either sets a new word to 1 or increases an existing word by 1

	for word in words:
		currentWord = word.lower().strip(',.:;\'\"&!?-_')
		if currentWord in wordCollection:
			wordCollection[currentWord] += 1
		else:
			wordCollection[currentWord] = 1
		
#Prints all of the collections contents to stdout		

for currentWord in wordCollection:
	print ("%s : %s" % (currentWord, wordCollection[currentWord]))


