yearfields = ["approx_dat", "pub_date", "comp_date", "base_date", "field_chec", "image_year", "photo_2", "photo_insp", "image_date", "prelim_edi", "cmp_fr", "interim_ed", "printed", "printed_ci", "revised", "site_surve", "transport", "prov_editi", "mg_dcl", "photo_revi", "edition_of", "reprint"]
newfields = []
for field in yearfields:
    name = field + "_s"
    newfields.append(name)
    arcpy.AddField_management("Geodex1",name,"SHORT")
    expression = "\"[" + field + "]\""
    arcpy.CalculateField_management("Geodex1",name,expression)

for field in newfields:
    expression1 = field + " < 1800" 
    espression2 = field + " > 2015"
    arcpy.SelectLayerByAttribute_management("Geodex1","CLEAR_SELECTION")
    arcpy.SelectLayerByAttribute_management("Geodex1","NEW_SELECTION",expression1)
    arcpy.SelectLayerByAttribute_management("Geodex1","ADD_TO_SELECTION",expression2)
    count = arcpy.GetCount_management("Geodex1")
    if count < 1000:
        arcpy.CalculateField_management("Geodex1",field,"0")
    arcpy.SelectLayerByAttribute_management("Geodex1","CLEAR_SELECTION")
    
    
        
    