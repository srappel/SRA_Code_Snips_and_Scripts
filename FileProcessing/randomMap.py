'''
This script will grab a specified number of random maps from the AGS digital map archive
'''

import sys
import os
import re
import random

from os import listdir
from os.path import isfile, join
from shutil import copy2

workingDirectory = 'R:/Image_Archive/am - Maps/'
outputDirectory = 'H:/Departments/AGSL/GIS/Patrons/2019_04/Tim_Kaufenberg/TIFF2/'
numberOfMaps = 100

# get all files in the workingDirectory into one array
allFiles = []
for root, dirs, files in os.walk(workingDirectory):
    for file in files:
        if file.endswith(".tif"):
            allFiles.append(os.path.join(root, file))

selectedFiles = []

i = 0
while i < numberOfMaps:
    y = random.randint(0,len(allFiles))
    selectedFiles.append(allFiles[y])
    allFiles.pop(y)
    i += 1

i = numberOfMaps
for file in selectedFiles:
    copy2(file,outputDirectory)
    i -= 1
    print(file + " has been copied... " + str(i) + " maps remain")
 