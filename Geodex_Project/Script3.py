arcpy.SelectLayerByAttribute_management("Geodex","NEW_SELECTION","""isobar_ft IS NOT NULL""")
count = arcpy.GetCount_management("Geodex")
if count < 300000:
    arcpy.CalculateField_management("Geodex","ISO_TYPE","\"Iso Ft\"")