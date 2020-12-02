mxd = arcpy.mapping.MapDocument("CURRENT")
lyrs = arcpy.mapping.ListLayers(mxd)
fields = arcpy.ListFields(lyrs[0])
fieldlist = []
layerlist = []
remfields = ["OBJECTID","geom","record","location","run_date","x1_1","x2_1","y1_1","y2_1","shape_leng","shape_area","geom_Length","geom_Area","bf2","bf3","image_date"]

for field in fields:
	fieldlist.append(str(field.name))

for remfield in remfields:
	fieldlist.remove(remfield)

for lyr in lyrs:
	layerlist.append(str(lyr.name))

for lyr in lyrs:
    infeat = lyr
    arcpy.SelectLayerByAttribute_management(infeat,"CLEAR_SELECTION")
    orig_count= float(str(arcpy.GetCount_management(lyr)))
    thresh = orig_count * 0.85
    for field in fieldlist:
        clause = field + " IS NULL"
        arcpy.SelectLayerByAttribute_management(infeat,"NEW_SELECTION",clause)
        count = arcpy.GetCount_management(lyr)
        select_count = int(str(count))
        string = str(lyr.name)
        string2 = str(lyr.name) + "," + field + " has processed"
        if thresh <= select_count:
            if orig_count <> select_count:
                filename = "D:/Working/Most_Null/" + field + "_Count_Results.txt"
                txtFile = open(filename,"a")
                txtFile.write(string + '\n')
                txtFile.close()
        print string2
    arcpy.SelectLayerByAttribute_management(infeat,"CLEAR_SELECTION")
        