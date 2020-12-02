import arcpy
import os

workspace = "R:\\GIS_Data\\Milwaukee"
textfile = "D:\\Working\\R_Walk.txt"

txt = open(textfile, "a")
filess = []

for dirpath, dirnames, filenames in arcpy.da.Walk(workspace,datatype="FeatureClass"):
    for filename in filenames:
        filess.append(os.path.join(dirpath, filename))

for filee in filess:
    txt.write(filee)
        
txt.close()       
        