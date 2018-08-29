#! /usr/bin/env python3

# pw.py - An insecure password manager program.

PASSWORDS= {'email': 'paswordmail',
			'blog': 'passwordblog',
			'luggage': '12345' }


import sys, pyperclip
if len(sys.argv) < 2:
	print('Usage: python pw.py [account] - copy account password \n Add account name after pw.py')
	sys.exit()

account = sys.argv[1] 		# first command line adg is the account name	

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account + ' copied to clipboard.')
else:
	print('There is no account named ' + account)



