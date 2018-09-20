#! /usr/bin/env python3
# mapIt.py - opens a browser tab with google maps on the adress stored on clipboard or as a command line argument

import webbrowser, pyperclip, sys

if len(sys.argv) > 1:
	#Get adress from command line
	adress = ' '.join(sys.argv[1:])
else:
	#Get adress from clipboard	
	adress = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + adress)

