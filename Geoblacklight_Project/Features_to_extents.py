 ##############################
### Features to Extents Tool ###
###      For Shapefiles      ###
 ##############################

#Created by Stephen Appel (srappel930@gmail.com) 10/16/15

###INFO###
"""
This script iterates through a folder and its subfolders to find
feature classes, determine their bounding geometry, project that
bounding geometry to WGS1984, and then print the bounding geometry
to a text file.  Must set the parameters at the top in the parameters
section.
"""

###IMPORTS###
import sys
import arcpy
import os
from arcpy import env
from arcpy import da

###Parameters###
#The directory holding the shapefiles...
#This can iterate through subfolders:
featurespace = "R:\\GIS_Data\\Sheboygan_Co"

#Use this workpace for the bounding boxes in original proj:
#CAUTION:(This folder's contents are deleted at the beginning of the script)
workspace = "D:\\Metadata"

#Use this workspace for the projected bounding boxes (don't change without
#Changing references in the first loop below):
#CAUTION:(This folder's contents are deleted at the beginning of the script)
workspace2 = workspace + "\\Proj"

#Use a prj file that uses ESPG: 4326 (WGS 1984)
OutCS = "D:\\x.prj"

#This is the name of the text file you will write the extents to:
filename = "D:\\ShebExtents.txt"

 #############
### Scripts ###
 #############

env.workspace = workspace
env.overwriteOutput = True
    
feature_paths = []
feature_name = []
exceptions = []

#Write the header on the output
f = open(filename, "w")
f.write("path;georss_box_s;solr_geom" + '\n')

#Delete features that are already in the working folders
#Exception here may indicate schema locks
fcs = arcpy.ListFeatureClasses()
if len(fcs) > 0:
    for fc in fcs:
        arcpy.Delete_management(fc)

    print "Features Deleted"
else:
    print "No Features to Delete"

#This uses the Walk function to search for feature classes... this datatype could be changed:
for dirpath, dirnames, filenames in da.Walk(featurespace,datatype="FeatureClass"):
    for filename in filenames:
        feature_paths.append(os.path.join(dirpath, filename))
        feature_name.append(str(filename))

print "Walk Complete"

#If the walk finds nothing, no need to go on...
if len(feature_paths) == 0:
    f.write("No features were found in the selected featurespace" + '\n')
    
#This loop takes each feature class and creates a minimum bounding geometry
#The second part of the loop, in the try statement, attempts to project
#if the project fails, it indicates that the original FC was not projected:
i = 0
while i < len(feature_paths):
    feature = feature_paths[i]
    name = str(feature_name[i])[:-4] + "_bounds.shp"
    outname = "Proj\\" + name[:-4] + "_prj.shp"
    arcpy.MinimumBoundingGeometry_management(feature,name,"ENVELOPE","ALL")
    try:
        arcpy.Project_management(name, outname,OutCS)
    except:
        print outname + "Failed to Project"
        exceptions.append(feature_paths[i])
    i += 1

#Switch the the second workspace where the projected features are now stored
env.workspace = workspace2

#Get the projected features, describe them, and write the formatted extents
#to the text file
fcs = arcpy.ListFeatureClasses()
for fc in fcs:
    desc = arcpy.Describe(fc)
    extent = desc.extent
    name = featurespace + "\\" + str(fc)[:-15] + ".shp;"
    #S,W,N,E
    write1 = name + "{0} {1} {2} {3};".format(extent.YMin,extent.XMin,extent.YMax,extent.XMax)
    #W,E,N,S
    write2 = "ENVELOPE({0},{1},{2},{3})".format(extent.XMin,extent.XMax,extent.YMax,extent.YMin)    
    f.write(write1 + write2 + '\n')
    print write

#Close the text file after printing exceptions at the bottom
if len(exceptions) > 0:
    f.write("Exceptions in layers: " + '\n')
    for ex in exceptions:
        f.write(ex + '\n')
else:
    f.write("There were no exceptions")

#Clear the working folder and subfolder:
try:
    for fc in fcs:
        arcpy.Delete_management(fc)
except:
    print "Exception when deleting features in " + workspace2 + "!"
env.workspace = workspace

try:
    fcs = arcpy.ListFeatureClasses()
    for fc in fcs:
        arcpy.Delete_management(fc)
except:
    print "Exception when deleting features in " + workspace + "!"

f.close()

 #########  
### FIN ###  
 #########