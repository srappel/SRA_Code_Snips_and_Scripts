#Script will look through a text file with ContentDM metadata extracts for compound objects and look for
#compound objects and then expand them to list all of their parts.

import re
import sys

'''
Example:
"am007221 through am007228"
Will be translated to
am007221
am007222
am007223
am007224
am007225
am007226
am007227
am007228

Other Types:
am007112 - am007123 (12 sheets)
agsmap024092_001-028
agsmaps023993 a and b
'''

#Step 1: get the input text tile as an argument
fileName = sys.argv[1]
outFile = sys.argv[2]

#Step 2: Get the text
with open(fileName, 'r') as myFile:
    contents = myFile.read()

#Step 2.1: Define a function for printint the regex results into a file.

def amWriteResults(inputList):
    for item in inputList:
        lowEndStr = item[0]
        highEndStr = item[1]
        lowEndInt = int(lowEndStr[2:])
        highEndInt = int(highEndStr[2:])
        typeOneRange = range(lowEndInt, highEndInt + 1)
        with open(outFile, 'a') as myOutFile:
            for i in typeOneRange:
                stri = str(i)
                stringLength = len(stri)
                numZeros = 6 - stringLength
                zeros = '0' * numZeros
                outString = 'am' + zeros + str(i) + '\n'
                
                myOutFile.write(outString)
                    
    myOutFile.close()
    inputlist = []


#Step 3: Define the regex for Type 1: am###### through am######
typeOneRegex = re.compile(r'(am\d\d\d\d\d\d) through (am\d\d\d\d\d\d)')

#Step 4: Split the components of the tuple and create the new numbers
typeOneList = typeOneRegex.findall(contents)
if len(typeOneList) > 0:
    print('There are type 1 results')
    amWriteResults(typeOneList)

#Type 2: am007112 - am007123 (12 sheets)

typeTwoRegex = re.compile(r'(am\d\d\d\d\d\d) - (am\d\d\d\d\d\d)')

typeTwoList = typeTwoRegex.findall(contents)
if len(typeTwoList) > 0:
    print('There are type 2 results')
    amWriteResults(typeTwoList)

myFile.close()

	
	

