#! /usr/bin/env python3

# mcb.pyw - saves and loads pieces of text to the clipboard.
# Usage:	./mcb.pyw save <keyword> 	- Saves clipboard to keyword.
# 			./mcb.pyw <keyword> 		- Loads keyword to clipboard.
#			./mcb.pyw list 				- Loads all keywords to clipboard.
# Usage:	./mcb.pyw del <keyword> 	- Remove keyword from shelve.
#			./mcb.pyw deleteall			- Deletes all the keywords

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content. 

if len(sys.argv) == 3: 
	if sys.argv[1].lower() == 'save':
		mcbShelf[sys.argv[2]] = pyperclip.paste()
	# Delete a key	
	elif sys.argv[1].lower() == 'del' and sys.argv[2] in mcbShelf :
		del mcbShelf[sys.argv[2]]	

elif len(sys.argv) == 2:
	# List keywords and load content. 
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	# Delete all the keys
	elif sys.argv[1].lower() == 'deleteall':
		for i in range(len(mcbShelf.keys())):
			del mcbShelf[(list(mcbShelf.keys()))[i]]
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])	


mcbShelf.close()
