#! /usr/bin/env python3
# selectiveCopy.py - A function that walks through a folder tree (origin) and searches for files with certain file extension (ext). 
# Then copies these files to new folder (destination).

import os, shutil

def selectiveCopy(origin, destination, ext):

	origin = os.path.abspath(origin)
	destination = os.path.abspath(destination)

	# TODO: walk the folder tree looking for .ext files
	for folderName, subfolders, filenames in os.walk(origin):
		print('Checking for ' + str(ext) + ' files in: ' + folderName)
		for subfolder in subfolders:
			print('Checking for ' + str(ext) + ' files in: ' + subfolder)
		for filename in filenames:
			if 	filename.endswith(str('.' + ext)):
				
				# Copy files to destination
				print('Coping %s...' % (filename))
				shutil.copy(os.path.join(folderName,filename), destination)

	print('Done')



selectiveCopy('./txtFiles', './desti', 'txt')