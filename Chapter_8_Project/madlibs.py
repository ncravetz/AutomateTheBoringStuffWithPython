#! /usr/bin/env python3

# madlibs.py - after asking for an ADJECTIVE, two NOUNs, an ADVERB or VERB creates a file with a phrase using those.

import shelve, os

madShelf = shelve.open('madlibsdb')

madShelf['ADJECTIVE'] = ''
madShelf['NOUN1'] = ''
madShelf['VERB'] = ''
madShelf['NOUN2'] = ''

# Ask the user for what words to use
print('Enter an adjective:')
madShelf['ADJECTIVE'] = input()

print('Enter a noun:')
madShelf['NOUN1'] = input()

print('Enter a verb:')
madShelf['VERB'] = input()

print('Enter another noun:')
madShelf['NOUN2'] = input()



# Creates a file with the phrase using those words


madFile = open('madlibsFile.txt', 'w')

madFile.write('The ' + str(madShelf['ADJECTIVE']) + ' panda walked to the ' + str(madShelf['NOUN1']) + 
	' an then ' + str(madShelf['VERB']) + '. A nearby ' + str(madShelf['NOUN2']) + ' was unaffected by these events.') 


madFile.close()



madShelf.close()