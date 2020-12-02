"""
This python script checks throught he current GEODEX style layers in a map document
and checks to see if both edition_no and edition_of are both not null for
half or more of the layer.  The use of this script helps to determine if the
edition_of and edition_no fields can be combined to a single "edition" field.

NOT A STANDALONE SCRIPT, MUST BE USED IN PYTHON WINDOW IN ARCMAP

Created by Stephen Appel 9/30/15 at the AGS Library

Notes:
-Uses the "CURRENT" mxd and loaded layers (all the layers
-Writes to a txt file on the D drive, to change, edit the "filename" variable
-clause variable could easily be edited to check other clauses.
-treshval is set to check if at least half of the values are not null for both, could be changed
"""

#definitions
mxd = arcpy.mapping.MapDocument("CURRENT")
lyrs = arcpy.mapping.ListLayers(mxd)
filename = "D:/Working/Edition/Edition_Count_Results.txt"
clause = "edition_no IS NOT NULL AND edition_of IS NOT NULL"
threshval = 0.5

#loop
for lyr in lyrs:
    infeat = lyr
    #clears the selection to get accurage feature count
    arcpy.SelectLayerByAttribute_management(infeat,"CLEAR_SELECTION")
    orig_count= int(str(arcpy.GetCount_management(lyr)))
    #Selects features based on the clause
    arcpy.SelectLayerByAttribute_management(infeat,"NEW_SELECTION",clause)
    select_count = int(str(arcpy.GetCount_management(lyr)))
    #sets the threshold value based on the threshval
    thresh = float(orig_count) * threshval
    if select_count >= thresh:
        txtFile = open(filename,"a")
        pct = select_count / orig_count
        #prints the layer name, the number of features that use both edition_no and edition_of, and the
        #proportion of records in the file that use both, comma delimited
        string = str(lyr.name) + "," + str(select_count) + "," + str(pct)
        txtFile.write(string + '\n')
        txtFile.close()
    #clears the selection so there are not a bunch of lingering selected features
    arcpy.SelectLayerByAttribute_management(infeat,"CLEAR_SELECTION")
    string2 = "Finished checking " + str(lyr.name)
    #prints a confirmation message to the python window in arc map
    print string2
    
    