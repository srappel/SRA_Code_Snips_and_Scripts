#This script looks through a workspace (dir)
#It will find all files and check if it has a .xml extension
#If it does, it will make sure it isn't an .aux.xml file
#It will then copy the files to a destination (destpath)

#Input paths:
dir = "R:\\GIS_Data\\" #The parent folder.  Script will look through the hirearchy below this directory
dest = "C:\\Workspace\\MetadataFiles" #This is a directory where the files will be copied to

#imports
import os
import shutil
from shutil import copy

#walk (Look for files as it walks through directory structures
for root, dirs, files in os.walk(dir): #set up walk
    for file in files: #iterate through files in the walk
        if file.endswith(".xml"): #find .xml files
            if not file.endswith(".aux.xml"): #Elminate aux.xml (raster auxillary files)
                print(os.path.join(root, file)) #print the path to the shell
                copy(os.path.join(root, file), dest) #copy to the destination folder.
