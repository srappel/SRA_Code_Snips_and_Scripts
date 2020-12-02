"""
This script iterates through the "workspace" and gets the path for each feature class
This will grab shapefiles that are points, lines, or polygons
"""
#Set the workspace to the folder you want to search for feature classes in
workspace = "R:\\GIS_Data\\Milwaukee\\Census_ALL"

#The path of a text file to write the path results, will be created
#if it doesn't exist.  To append to an existing file, change "w" to "a"
txtFile = open("D:/DatasetList.txt", "w")


#imports
import arcpy
import os

feature_classes = []

#walk (Look for feature classes)
for dirpath, dirnames, filenames in arcpy.da.Walk(workspace,datatype="FeatureClass"):
    for filename in filenames:
        feature_classes.append(os.path.join(dirpath, filename))
for fc in feature_classes:
    txtFile.write(fc + '\n')

txtFile.close()    
