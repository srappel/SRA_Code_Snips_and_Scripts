layer = ""
fieldlist = ["approx_dat","pub_date","comp_date","base_date",
             "edition_no","field_chec","photo_2",
             "photo_insp","cmp_fr",
             "interim_ed","printed","revised",
             "site_surve","prov_editi","photo_revi","edition_of",
             "reprint"]

where = """p_date = '0' AND """ + fieldlist[0] + " IS NULL AND "+ fieldlist[1] + " IS NULL AND " + fieldlist[15] + " IS NULL AND " + fieldlist[2] + " IS NULL AND " + fieldlist[3] + " IS NULL AND " + fieldlist[4] + " IS NULL AND " +fieldlist[5] + " IS NULL AND " + fieldlist[6] + " IS NULL AND " + fieldlist[7] + " IS NULL AND " +fieldlist[8] + " IS NULL AND " + fieldlist[9] + " IS NULL AND " + fieldlist[10] + " IS NULL AND " + fieldlist[11] + " IS NULL AND " + fieldlist[12] + " IS NULL AND " + fieldlist[13] + " IS NULL AND " +fieldlist[14] + " IS NULL AND " + fieldlist[15] + " IS NULL AND " +fieldlist[16] + " IS NULL"

arcpy.SelectLayerByAttribute_management(layer,"NEW_SELECTION",where)
arcpy.GetCount_management(layer)