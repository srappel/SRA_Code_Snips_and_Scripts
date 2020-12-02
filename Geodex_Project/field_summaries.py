mxd = arcpy.mapping.MapDocument("CURRENT")
lyrs = arcpy.mapping.ListLayers(mxd)
fields = arcpy.ListFields(lyrs[0])
fieldlist = []
layerlist = []
remfields = ["OBJECTID","geom","record","location","run_date","x1_1","x2_1","y1_1","y2_1","shape_leng","shape_area","geom_Length","geom_Area"]

for field in fields:
	fieldlist.append(str(field.name))

for remfield in remfields:
	fieldlist.remove(remfield)

for lyr in lyrs:
	layerlist.append(str(lyr.name))

for lyr in lyrs:
    infeat = lyr
    arcpy.SelectLayerByAttribute_management(infeat,"CLEAR_SELECTION")
    orig_count= int(str(arcpy.GetCount_management(lyr)))
    for field in fieldlist:
        clause = field + " IS NULL"
        arcpy.SelectLayerByAttribute_management(infeat,"NEW_SELECTION",clause)
        count = arcpy.GetCount_management(lyr)
        select_count = int(str(count))
        string = str(lyr.name)
        string2 = str(lyr.name) + "," + field + " has processed"
        if orig_count == select_count:
            filename = "D:/Working/All_Null/" + field + "_Count_Results.txt"
            txtFile = open(filename,"a")
            txtFile.write(string + '\n')
            txtFile.close()
        else:
            filename = "D:/Working/Not_All_Null/" + field + "_Count_Results.txt"
            txtFile = open(filename,"a")
            txtFile.write(string + '\n')
            txtFile.close()
        print string2
        
        