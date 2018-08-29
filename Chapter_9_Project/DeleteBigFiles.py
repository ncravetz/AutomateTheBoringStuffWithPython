#! /usr/bin/env python3
# DeleteBigFiles.py - Walk a folder and find files bigger than a 100MB.

import os, shutil, pprint
bigFiles = []

# Walk Folder

for folderName, subfolders, filenames in os.walk('./Movies'):
	for filename in filenames:
		if os.path.getsize(os.path.join(folderName,filename)) >= 100000000:
			bigFiles.append(filename)






# Print file list

print('This files are bigger than 100MB:')
#pprint.pprint(bigFiles)
print '\n'.join(bigFiles)
