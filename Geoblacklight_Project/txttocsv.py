import csv

#Transfer txt file to csv file
rawContent = open("all.txt", 'r')
x = [line.rstrip() for line in rawContent.readlines()] #read every line of the file and cut the '\n' in the end for each line 
#x = [line for line in x if line !='']
myfile = open('all2.csv','w')
for i in x:
	#print str(i)
	if str(i) == ",AGSL DIGITAL SPATIAL DATA CLEARINGHOUSE Readme File":
		myfile.write('\n' + str(i))
	else:
		myfile.write(str(i))
myfile.close()
raw_input()
