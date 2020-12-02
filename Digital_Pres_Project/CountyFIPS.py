#Iterate through datasets in TIGER folder
#Grab the county fips from the file name and save as variable
#Create a new field in each dataset called CO_FIPS
#Calculate new field with value pulled from filename
#Merge all the shapefiles into one

import arcpy

workspace = "C:/Workspace/TIGER"
arcpy.env.workspace = workspace

for dirname, dirnames, filenames in arcpy.da.Walk(workspace): #Iterate through folder
    for filename in filenames:
	    FIPS = filename[8:13]
	    print FIPS + " " + filename
	    arcpy.AddField_management(filename,"COFIPS","TEXT","","",5)
	    arcpy.CalculateField_management(filename,"COFIPS",FIPS)
		
		
	
	
