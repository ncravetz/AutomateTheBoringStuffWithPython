#! /usr/bin/env python3

# madlibs.py - after asking for an ADJECTIVE, two NOUNs, an ADVERB or VERB creates a file with a phrase using those.

import os



# Ask the user for what words to use
print('Enter an adjective:')
ADJECTIVE = input()

print('Enter a noun:')
NOUN1 = input()

print('Enter a verb:')
VERB = input()

print('Enter another noun:')
NOUN2 = input()



# Creates a file with the phrase using those words


madFile = open('madlibsFile2.txt', 'w')

madFile.write('The ' + str(ADJECTIVE) + ' panda walked to the ' + str(NOUN1) + 
	' an then ' + str(VERB) + '. A nearby ' + str(NOUN2) + ' was unaffected by these events.') 


madFile.close()


