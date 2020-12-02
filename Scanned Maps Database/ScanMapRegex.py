#Script will run through a text file with non-standardized text and try to find an extract AGS Scan Numbers
#Scan numbers will be written to a new text file with one scan number per line
import sys
import re

#Step 1: get the input text tile as an argument
fileName = sys.argv[1]
outFile = sys.argv[2]

#Step 2: Get the text
with open(fileName, 'r') as myFile:
    contents = myFile.read()

#Step 3: Define the regex

agsScanRegex1 = re.compile(r'agsmap\d\d\d\d\d\d_\d\d\d|agsmap\d\d\d\d\d\d_\D')

agsScanList1 = agsScanRegex1.findall(contents)


#Type 2:

agsScanRegex2 = re.compile(r'agsmap\d\d\d\d\d\d|am\d\d\d\d\d\d')

agsScanList2 = agsScanRegex2.findall(contents)



with open(outFile, 'a') as myOutFile:
    for i in agsScanList1:
        string = i + '\n'
        myOutFile.write(string)

    for i in agsScanList2:
        string = i + '\n'
        myOutFile.write(string)

myOutFile.close()
myFile.close()



