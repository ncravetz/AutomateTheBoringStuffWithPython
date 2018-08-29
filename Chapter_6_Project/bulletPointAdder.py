#! python3

# bulletPointAdder.py - Adds bullet points to the start of each line of each text on the clipboard.

import pyperclip

text = pyperclip.paste()

# Separate lines and add stars.

lines = text.split('\n')
for i in range(len(lines)):			# Loop through all the lines
	lines[i] = '* ' + lines[i]		# Add '* ' before each line

text = '\n'.join(lines)
	


# add text to the clipboard
pyperclip.copy(text)

