"""
This script iterates through Geodex style layers in a map document to determine
the usage of the year fields (listed below in array "fieldlist".

The script considers the field "used" if less than 15% of the values are null.  If
the field is used, it adds one to the fieldsused count.  When its finished checking
all the fields for a layer, it will print a statement to the text file that contains
the file name,the count of used year fields, a list of the year fields

Created by Stephen Appel 9/30/15 at the AGS Library

THIS IS NOT A STANDALONE SCRIPT, MUST BE USED IN THE PYTHON WINDOW IN ARCMAP.
"""

#definitions
mxd = arcpy.mapping.MapDocument("CURRENT")
lyrs = arcpy.mapping.ListLayers(mxd)
#lyrs = ["f0002","f0150"]
filename = "D:/Working/YearFields/Year_Fields_Counts.txt"
fieldlist = ["approx_dat","pub_date","comp_date","base_date",
             "edition_no","field_chec","photo_2",
             "photo_insp","cmp_fr",
             "interim_ed","printed","revised",
             "site_surve","prov_editi","photo_revi","edition_of",
             "reprint"]
threshval = 0.75
fieldnames = []
lyrfields = []

#loop
i = 0

for lyr in lyrs:
    fieldsused = 0
    lyrfields = []
    infeat = lyr
    arcpy.SelectLayerByAttribute_management(infeat,"CLEAR_SELECTION","")
    orig_count = int(str(arcpy.GetCount_management(lyr)))
    thresh = orig_count * threshval
    for field in fieldlist:
        clause = field + " IS NULL"
        arcpy.SelectLayerByAttribute_management(infeat,"NEW_SELECTION",clause)
        count = int(str(arcpy.GetCount_management(infeat)))
        if count < thresh:
            fieldsused += 1
            lyrfields.append(field)
        arcpy.SelectLayerByAttribute_management(infeat,"CLEAR_SELECTION","")

    txtFile = open(filename,"a")
    string = str(lyr) + "," + str(fieldsused) + ",("
    txtFile.write(string)
    for fld in lyrfields:
        txtFile.write(fld + ";")
    txtFile.write(")" +'\n')
    txtFile.close()
    print str(lyr) + " has been processed"


