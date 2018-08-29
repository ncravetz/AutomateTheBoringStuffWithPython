#! Python3

# strongPassword.py - Checks if a password is strong.
# More than 8 characters | Upper and lower case | At least one number

import re

noSpace = re.compile(r'\s')
upperCase = re.compile(r'[A-Z]')
lowerCase = re.compile(r'[a-z]')
hasNumber = re.compile(r'\d')


def strongPass(text):
	
	if noSpace.search(text) != None:
		print(text + ' <-- The password is not strong. It has a space in it')
		

	elif len(text) < 8:
		print(text + ' <-- The password is not strong. It is less than 8 characters')
		

	elif upperCase.search(text) == None:
		print(text + ' <-- The password is not strong. It has no upper case characters')
		

	elif lowerCase.search(text) == None:
		print(text + ' <-- The password is not strong. It has no lower case characters')	
		

	elif hasNumber.search(text) == None:
		print(text + ' <-- The password is not strong. It has no numbers')		
		

	else:
		print(text + ' <-- This is a strong password')	



strongPass('saissaf')
strongPass('saisSDFs7af')
strongPass('sais. saf')
strongPass('sais saf')
strongPass('saissdsafasdsaf')
strongPass('HDJDDICIVDDD0')
