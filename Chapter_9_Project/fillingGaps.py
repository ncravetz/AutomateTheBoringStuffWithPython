#! /usr/bin/env python3
# fillingGaps.py - Rename files starting with 'spam' to number them correctly without spaces.

import os, shutil, re

spamFiles = []

spamNumber=re.compile(r'(spam)(\d\d\d\d)(\.txt)')

# Get all the files on the folder
allFiles = os.listdir('./txtFiles')

for x in range(len(allFiles)):
	if spamNumber.search(allFiles[x]) != None:
		spamFiles.append(str(allFiles[x]))



# Check for ideally named files. Make a while loop looking for the next one that breaks at the rename.

idealFile = ''

for i in range(len(spamFiles)):
	idealFile = 'spam' + str(str(i+1).zfill(4)) + '.txt'		# Not considering cases of spam029.txt 
	if idealFile not in spamFiles:
		M = 1
		while True:
			nextFile = 'spam' + str(str(i+1+M).zfill(4)) + '.txt'
			if nextFile in spamFiles:
				# Rename item in list, print rename, rename file in folder
				print('Renaming ' + str(nextFile) + ' to ' + str(idealFile))
				shutil.move(str('./txtFiles/' + nextFile), str('./txtFiles/' + idealFile))
				spamFiles[spamFiles.index(nextFile)] = idealFile

				break
			M = M +1	
	else:
		continue





	




