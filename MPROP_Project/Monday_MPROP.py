import time     #need the time module to add stamps to the file names
import urllib2  #to get data from websites
import os       #SRA - Added this so a directory can be created

#from Python docs How to Fetch Internet Resources Using urllib2:

#"HTTP is based on requests and responses - the client makes requests and servers send responses.
#urllib2 mirrors this with a Request object which represents the HTTP request you are making.
#In its simplest form you create a Request object that specifies the URL you want to fetch.
#Calling urlopen with this Request object returns a response object for the URL requested.
#This response is a file-like object, which means you can for example call .read() on the response:"

timestamp = time.strftime('%y%m%d_') #This uses the time module to pull the current time and format how you want it to look #SRA- Edited the timestamp to match previous conventions
path = "H:/Departments/AGSL/GIS/Projects/MPROP_Auto/Downloads/" + timestamp + "Extract" #SRA - This defines a path for the directory that will be created to house the new extract

print "Creating Path " + path

#Check if the path already exists and create the directory if it doesn't
#Note that the directory SHOULDNT exist, not sure why it would or what would happen if it did
if not os.path.exists(path):
	os.makedirs(path)

print "Downloading Parcelbase" #Confirm to the user that the download has started

PBresponse = urllib2.urlopen('http://itmdapps.milwaukee.gov/gis/mapdata/parcelbase.zip')  #From City's MPROP page that lists
                                                                                        #various formats, click the download you
                                                                                        #want. The address will briefly appear
                                                                                        #in a new tab. Copy that URL and paste here.
                                                                                        #(You can also right-click the download
                                                                                        #link and chose "Copy Link Address")
html = PBresponse.read()    #See above comment from Python doc^^


with open(path + "/" + timestamp + 'Parcelbase.zip','wb') as f:      #write download to whereever you want(and use timestamp to date it)
    f.write(html)													 #SRA - modified to add the path to the new directory.

print "Parcelbase download complete"        #tell user download is complete

print "Downloading MAI" #Confirm to the user that the download has started

MAIresponse = urllib2.urlopen('http://itmdapps.milwaukee.gov/xmldata/Get_mai_xml')  #repeat these steps twice more:
                                                                                    #another time for MAI, and once more for MPROP
                                                                                    #Only changes are the URLs, file/variable names
                                                                                    #and extention formats (.zip v .xsls)
html = MAIresponse.read()

with open(path + "/" + timestamp + 'MAI.xml','wb') as f:
    f.write(html)

print "MAI download complete"
print "Downloading MPROP" #Confirm to the user that the download has started

MPROPresponse = urllib2.urlopen('http://itmdapps.milwaukee.gov/xmldata/Get_mprop_xml')
html = MPROPresponse.read()

with open(path + "/" + timestamp + 'MPROP.xml','wb') as f:
    f.write(html)

print "MPROP download complete"
