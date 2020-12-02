orig_count = arcpy.GetCount_management(layer)
arcpy.AddField_management(layer,"holding1","SHORT")
arcpy.SelectLayerByAttribute_management(layer,"NEW_SELECTION","""holding = 'YES'""")
yes_count = arcpy.GetCount_management(layer)
if yes_count <> orig_count:
    arcpy.CalculateField_management(layer,"holding1","1")
arcpy.SelectLayerByAttribute_management(layer,"NEW_SELECTION","""holding = 'NO'""")
no_count = arcpy.GetCount_management(layer)
if no_count <> orig_count:
    arcpy.CalculateField_management(layer,"holding1","0")