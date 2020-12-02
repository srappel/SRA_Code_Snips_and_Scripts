import arcpy
import os

workspace = "R:/GIS_Data/USA/Flood_All/Q3_Flood_FEMA"
featureclasses = []
walk = os.walk(workspace)

for dirpath, dirnames, filenames in walk:
	for filename in filenames:
		if filename.endswith(".e00"):
			featureclasses.append(os.path.join(dirpath, filename))
		
		
For featureclass in featureclasses:
	arcpy.ImportFromE00_conversion(featureclass,"C:/Workspace/Flood_All/")
		
workspace = "C:/Workspace/Flood_All/"
walk = arcpy.da.Walk(workspace)
featureclasses = []

if os.path.isdir("C:/Workspace/Flood_All2/") is False:
	os.mkdir("C:/Workspace/Flood_All2/")

for dirpath, dirnames, filenames in walk:
	for filename in filenames:
		if not filename.endswith("scale"):
			if not filename.endswith("igds.txt"):
				if not filename.endswith("igds"):
					featureclasses.append(os.path.join(dirpath, filename))
		
for featureclass in featureclasses:
	a,b,c,d = featureclass.rsplit("\\",3)
	dir = a + "2/" + b
	if os.path.isdir(dir) is False:
		os.mkdir("C:/Workspace/Flood_All2/" + c)
	arcpy.FeatureClassToShapefile_conversion(featureclass,"C:/Workspace/Flood_All2/" + c)
	
	