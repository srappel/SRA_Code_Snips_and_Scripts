#definitions
mxd = arcpy.mapping.MapDocument("CURRENT")
#lyrs = arcpy.mapping.ListLayers(mxd)
lyrs = ["f0309"]
filename = "D:/Working/XY_check/X_Y_180.txt"

#loop
for layer in lyrs:
    arcpy.SelectLayerByAttribute_management(layer,"CLEAR_SELECTION")
    cursor = arcpy.SearchCursor(layer)
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    txtFile = open(filename,"a")
    
    for row in cursor:
        x1val = row.getValue("x1_1")
        x2val = row.getValue("x2_1")
        #y1val = row.getValue("y1_1")
        #y2val = row.getValue("y2_1")
        oids = []
        thresh = 178
        if x2val > thresh:
            st = row.getValue("OBJECTID")
            print str(st)
            oids.append(row.getValue("OBJECTID"))
            
            
    string = str(layer.name) +  ": " + str(oids) + '\n'
    txtFile.write(string)
    txtFile.close()