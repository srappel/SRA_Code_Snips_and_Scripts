# Import system modules
import arcpy
from arcpy import env
 
try:
    # Set the workspace (to avoid having to type in the full path to the data every time)
    env.workspace =  "D:/Geodex.gdb"
    
    # Set local parameters
    inFeatures = "Geodex"
 
    # Process: Set Subtype Field...
    arcpy.SetSubtypeField_management(inFeatures, "GDX_FILE")
     
    # Process: Add Subtypes...
    # Store all the suptype values in a dictionary with the subtype code as the "key" and the 
    # subtype description as the "value" (stypeDict[code])
    stypeDict = {} 

    cursor = arcpy.SearchCursor("GDX_FILES")

    for row in cursor:
        key = row.getValue("GDX_FILE")
        value = row.getValue("DESC")
        stypeDict[key] = value
    del row
    del cursor
    stypeDict[0] = "Not Assigned"
    
    # use a for loop to cycle through the dictionary
    for code in stypeDict:
        arcpy.AddSubtype_management(inFeatures, code, stypeDict[code])     
			
    # Process: Set Default Subtype...
    arcpy.SetDefaultSubtype_management(inFeatures, "0")
 
except Exception, e:
    # If an error occurred, print line number and error message
    import traceback, sys
    tb = sys.exc_info()[2]
    print "Line %i" % tb.tb_lineno
    print e.message