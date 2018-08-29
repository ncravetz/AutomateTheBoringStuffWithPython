#! /usr/bin/env python3
# renameDates.py - Rename filenames with american date format MM-DD-YYYY to european date format DD-MM-YYYY

import os, shutil, re

# Create a regex that matches files with the american date format

datePattern = re.compile(r"""^(.*?)	# all text before the date
	((0|1)?\d)-						# one or two digits for the month starting with 0 ir 1
	((0|1|2|3)?\d)-					# one or two digits for the day starting with 0, 1, 2 or 3
	((19|20)\d\d)					# four digits for the year starting with 19 or 20
	(.*?)$
	""", re.VERBOSE)


# Loop over the files in the current working directory

for amerFilename in os.listdir('.'):
	mo = datePattern.search(amerFilename)

	# Skip files without a date
	if mo == None:
		continue

	# Get the diferent parts of the filename
	beforePart 	= mo.group(1)
	monthPart 	= mo.group(2)
	dayPart 	= mo.group(4)
	yearPart 	= mo.group(6)
	afterPart	= mo.group(8)


	# Form the european style Filename

	euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

	# Get the full, absolute file path

	absWorkingDir = os.path.abspath('.')
	amerFilename = os.path.join(absWorkingDir, amerFilename)
	euroFilename = os.path.join(absWorkingDir, euroFilename)

	# Rename the files
	print('Renaming "%s" to "%s"...' % (amerFilename,euroFilename))
	#shutil.move(amerFilename,euroFilename)


