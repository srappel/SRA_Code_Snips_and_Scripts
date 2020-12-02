'''
This python program needs to be run on the command line.  It accepts one argument, that is,
the folder you would like to search for missing AGS scan numbers.

This system is not perfect, but should alert you to abnormalities in the sequence of scan
numbers in a file folder.  It will search both am or agsmap style scan numbers and can
even identify missing sheet numbers in a set or missing sides.

To use.  Open a command line and navigate to the folder containing the python program.
Then run using python and one argument:

ie.

python imageArchiveChecker_V2.py "r:\image_archive\am00100 - am00199"

It should run for python 2 or python 3
'''

import sys
import os
import re

from os import listdir
from os.path import isfile, join

workingDirectory = sys.argv[1] #Enter a directory path to search for missing numbers in the sequence
outputFile = sys.argv[2] #Enter a directory path for the output file
recursiveInterogative = sys.argv[3]

if recursiveInterogative == '/r':
	#get the files if recursive is True
	onlyFiles = []
	for folderName, subfolders, filenames in os.walk(workingDirectory):
		for filename in filenames:
			onlyFiles.append(filename)
else:
#get the files if recursive is false
	onlyFiles = [f for f in listdir(workingDirectory) if isfile(join(workingDirectory, f))]

#Create a list of all the scan numbers using a regex to pull out any non-scan files
scanNumRegex = re.compile(r'(agsmap|am)(\d\d\d\d\d\d)(\w*)?')

nonScans = [] #empty list to hold files that do not match a scanned map pattern
allScans = [] #empty list to hold filename that match the regex
allSuffix = [] #empty list to hold only filenames with a suffix
missingScans = [] #empty list to hold missing scans

for f in onlyFiles:
    ro = scanNumRegex.search(f)
    if not ro == None:
        fullScanNumber = ro.group(1) + ro.group(2) + ro.group(3)
        allScans.append(fullScanNumber)
        if not ro.group(3) == '':
            allSuffix.append(fullScanNumber)
    else:
        nonScans.append(f)
    ro == None
    
#Define the missing number function:
def isMissing(number, prevNum):
    if number != prevNum:
            if number != prevNum + 1:
                return True
            else:
                return False
    else:
        return False
    
#run through the all scans list and check for missing numbers in sequence

prevNum = ''
for f in allScans:
    ro = scanNumRegex.search(f)
    if not ro == None:
        number = int(ro.group(2))
        if prevNum== '':
            prevNum = number
			
        if isMissing(number, prevNum) == True:
            if number > 999999:
                num0 = ''
            elif number > 99999:
                num0 = ''
            elif number > 9999:
                num0 = '0'
            elif number > 999:
                num0 = '00'
            elif number > 99:
                num0 = '000'
            elif number > 9:
                num0 = '0000'
            else:
                num0 = '00000'
			
            missingScanNumber = ro.group(1) + num0 + str(int(ro.group(2)) - 1) + ro.group(3)
            missingScans.append(missingScanNumber)
        prevNum = number

#Now check for missing suffix in sets:
setRegex = re.compile(r'(agsmap|am)(\d\d\d\d\d\d)_(\d\d\d)(\w*)?')

prevNum = 0
prevSet = 0
setNumber = 0
sheetNumber = 0
fullScanNumber = ''

for f in allSuffix:
    ro = setRegex.search(f)
    if not ro == None:     
        setNumber = int(ro.group(2))
        sheetNumber = int(ro.group(3))
        if prevNum == 0:
            prevNum = sheetNumber
            prevSet = setNumber
        if isMissing(sheetNumber, prevNum) is True:
            if not sheetNumber == 1:
                if sheetNumber > 99:
                    num0 = ''
                elif sheetNumber > 9:
                    num0 = '0'
                else:
                    num0 = '00'
                missingScans.append(ro.group(1) + ro.group(2) + '_' + num0 + str(int(ro.group(3)) - 1) + ro.group(4))
        #check if there is a second suffix and check for missing second suffix
        if not ro.group(4) == '':
            if ro.group(4) == '_a':
                check = ro.group(1) + ro.group(2) + '_' + ro.group(3) + '_b'
                if not check in allSuffix:
                    missingScans.append(check)
            if ro.group(4) == '_b':
                check = ro.group(1) + ro.group(2) + '_' + ro.group(3) + '_a'
                if not check in allSuffix:
                    missingScans.append(check)
        prevNum = sheetNumber
        prevSet = setNumber

#finally do an a b check
abRegex = re.compile(r'(agsmap|am)(\d\d\d\d\d\d)(_[ab])')

for f in allSuffix:
    ro = abRegex.search(f)
    if not ro == None:
        if ro.group(3) == '_a':
            check = ro.group(1) + ro.group(2) + '_b'
            if not check in allSuffix:
                missingScans.append(check)
        if ro.group(3) == '_b':
            check = ro.group(1) + ro.group(2) + '_a'
            if not check in allSuffix:
                missingScans.append(check)

#Write Results to Output File				
file = open(outputFile, 'w')
file.write('Image Archive Check Results:' + '\n')
file.write('Total files in directory tree: ' + str(len(onlyFiles)) + '\n')
if len(nonScans) > 0:
	file.write('Total files not matching scan number format: ' + str(len(nonScans)) + ':\n')
	for f in nonScans:
		file.write(f + '\n')
file.write('\n')

if len(missingScans) > 0:
	file.write('There were ' + str(len(missingScans)) + ' detected missing scans:\n')
	for f in missingScans:
		file.write(f + '\n')

				
#Print Results:
print('Image Archive Check Results:' + '\n')
print('Total files in folder: ' + str(len(onlyFiles)) + '\n')
if len(nonScans) > 0:
    print('Total files not matching scan number format: ' + str(len(nonScans)) + ':')
    for f in nonScans:
        print(f)
    print('\n')
if len(missingScans) > 0:
    print('There were ' + str(len(missingScans)) + ' detected missing scans:')
    for f in missingScans:
        print(f)
        


