import arcpy
import string

#Get layers
mxd = arcpy.mapping.MapDocument("CURRENT")
lyrs = arcpy.mapping.ListLayers(mxd)

#Delete Unused Fields
delfields = ["bf1","bf2","bf3","bf4","image_date","image_year","interim_ed","prelim_edi","mg_dcl"]

for layer in lyrs:
    arcpy.DeleteField_management(layer,delfields) 

#Make new fields

#Add and calculate a scale field:
for layer in lyrs:
    arcpy.AddField_management(layer,"scale1","LONG")
    arcpy.CalculateField_management(layer,"scale1","!scale![8:]","PYTHON")

#Make and fill a numeric holding field (short integer)
    #Although it will only accept 1 and 0 now, it can
    #eventually be updated for multiple holdings.
for layer in lyrs:
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

    arcpy.SelectLayerByAttribute_management(layer,"CLEAR_SELECTION")    
        
#Move printed_ci values to printed
for layer in lyrs:
    orig_count = arcpy.GetCount_management(layer)
    arcpy.SelectLayerByAttribute_management(layer,"NEW_SELECTION","""printed IS NULL""")
    null_count = arcpy.GetCount_management(layer)

    if null_count < orig_count:
        #Check if printed_ci is all null
        arcpy.SelectLayerByAttribute_management(layer,"NEW_SELECTION","""printed_ci IS NULL""")
        null2_count = arcpy.GetCount_management(layer)
        if null2_count < orig_count:
            #Do something if not all are null
            arcpy.SelectLayerByAttribute_management(layer,"NEW_SELECTION","""printed_ci IS NOT NULL""")
            arcpy.CalculateField_management(layer,"printed","printed_ci")
        else:
            arcpy.SelectLayerByAttribute_management(layer,"CLEAR_SELECTION")
    else:
        arcpy.SelectLayerByAttribute_management(layer,"CLEAR_SELECTION")

    arcpy.SelectLayerByAttribute_management(layer,"CLEAR_SELECTION")
    
#fill "printed" with values from "printed_ci"
where = """printed IS NULL"""
for layer in lyrs:  
    arcpy.SelectLayerByAttribute_management(layer,"NEW_SELECTION",where)
    

#Replace the x1_1, x2_1, y1_1, and y2_1 fields with XW, XE, YN, YS fields
    #Must add the x and y domains to the geodatabase.
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









    
    