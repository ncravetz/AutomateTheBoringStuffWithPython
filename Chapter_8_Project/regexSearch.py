#! /usr/bin/env python3

# regexSearch.py - Ask the user for a regular expression and then search for matches in all the .txt files in a folder. Print all the matches

import os, re


# Ask the user for a regex and save it in a variable

print('What regex do you want to match?')
userRegex = input()



#	Finds all the txt files with os.listdir(path)
#	Makes a list with all the file names matching '.*\.txt'

txtList = []
txtType = re.compile(r'.*\.txt')
fileList = os.listdir('/Users/123seguro/txtFiles')



for i in range(len(fileList)):
	if txtType.search(str(fileList[i])) is not None: 
		txtList.append(fileList[i])




#TODO: Look for matches in all the files looping through the list

compiledUserRegex = re.compile(str(userRegex))
matches = []

for i in range(len(txtList)):
	openFile = open('/Users/123seguro/txtFiles/' + txtList[i]) 
	allText = openFile.read()
	matches.append(compiledUserRegex.findall(str(allText)))


#TODO: Print all the matches in the screen 
#TODO: put them all in one list and print them one per line



for i in range(len(matches)):
	for x in range(len(matches[i])):
		print(matches[i][x])







