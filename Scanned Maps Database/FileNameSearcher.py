import sys
import os
import re
import time

from os import listdir
from os.path import isfile, join

workingDirectory = sys.argv[1] #Enter a directory path to search for missing numbers in the 
searchString = sys.argv[2] #The string to be searched in the filename

#get the files
#onlyFiles = [f for f in listdir(workingDirectory) if isfile(join(workingDirectory, f))]
onlyFiles = []

for folderName, subfolders, filenames in os.walk(workingDirectory):
	for filename in filenames:
		onlyFiles.append(filename)
		
#Create a list of all the scan numbers using a regex to pull out any non-scan files
regexString = r'(agsmap|am)(\d\d\d\d\d\d)(_?' + searchString + r')'
scanNumRegex = re.compile(regexString)

matchingScans = []

for f in onlyFiles:
    ro = scanNumRegex.search(f)
    if not ro == None:
        fullScanNumber = ro.group(1) + ro.group(2) + ro.group(3)
        matchingScans.append(fullScanNumber)
    ro == None
    
#Open txt document for writing:
time = str(int(time.time()))

filename = 'C:\\users\\srappel\\desktop\\' + 'results_' + searchString + '_' + time + '.txt'
file = open(filename, 'w')
file.close()
file = open(filename, 'a')

if len(matchingScans) > 0:
	for f in matchingScans:
		file.write(f + '\n')

	


