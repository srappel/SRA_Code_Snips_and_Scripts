mxd = arcpy.mapping.MapDocument("CURRENT")
lyrs = arcpy.mapping.ListLayers(mxd)

newFields = ["XW","XE","YN","YS"]


for layer in lyrs:
    for field in newFields:
        if field == "XW" or "XE":
            arcpy.AddField_management(layer,field,"FLOAT",field_domain="x")
        elif field == "YN" or "YS":
            arcpy.AddField_management(layer,field,"FLOAT",field_domain="y")

    arcpy.SelectLayerByAttribute_management(layer,"CLEAR_SELECTION")
    arcpy.CalculateField_management(layer,"XW","!x1_1!","PYTHON")
    arcpy.CalculateField_management(layer,"XE","!x2_1!","PYTHON")
    arcpy.CalculateField_management(layer,"YN","!y1_1!","PYTHON")
    arcpy.CalculateField_management(layer,"YS","!y2_1!","PYTHON")

    print str(layer.name) + " has been processed..."