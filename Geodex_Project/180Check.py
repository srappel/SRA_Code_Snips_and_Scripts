#180ø Longitude X-over entry

#definitions
mxd = arcpy.mapping.MapDocument("CURRENT")
lyrs = arcpy.mapping.ListLayers(mxd)
#lyrs = ["f0309"]
filename = "D:/Working/XY_check/X_Y_180_Analysis.txt"

#Header
txtFile = open(filename,"a")
string = "Check for files with the 180 longitude map_format"
txtFile.write(string + '\n' + '\n')
txtFile.close()


#loop1

for layer in lyrs:
    arcpy.SelectLayerByAttribute_management(layer,"CLEAR_SELECTION")
    ocount = arcpy.GetCount_management(layer)
    arcpy.SelectLayerByAttribute_management(layer,"NEW_SELECTION","""map_format = '180ø Longitude X-over entry'""")
    ncount = arcpy.GetCount_management(layer)
    cursor = arcpy.SearchCursor(layer)
    txtFile = open(filename,"a")

    if ncount != ocount:
        count_string = str(ncount)
    else:
        count_string = "None"
              
            
    string = str(layer.name) + ": " + count_string
    txtFile.write(string + '\n')
    txtFile.close()

    print str(layer.name)


#Header
txtFile = open(filename,"a")
string = """Number of records not containing: map_format = '180ø Longitude X-over entry' but containing recrods on the 180th meridian"""
txtFile.write(string + '\n' + '\n')
txtFile.close()

#loop2 - Check for layers that probably should have some of those values, but are incorrectly labeled
for layer in lyrs:
    arcpy.SelectLayerByAttribute_management(layer,"CLEAR_SELECTION")
    ocount = arcpy.GetCount_management(layer)
    arcpy.SelectLayerByAttribute_management(layer,"NEW_SELECTION","""x2_1 = 180 AND map_format <> '180ø Longitude X-over entry'""")
    ncount = arcpy.GetCount_management(layer)
    cursor = arcpy.SearchCursor(layer)
    txtFile = open(filename,"a")

    if ncount != ocount:
        count_string = str(ncount) + "/" + str(ocount)
    else:
        count_string = "None"
              
            
    string = str(layer.name) + ": " + count_string
    txtFile.write(string + '\n')
    txtFile.close()

    print str(layer.name)    