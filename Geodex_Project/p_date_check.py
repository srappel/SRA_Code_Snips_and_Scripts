'''
Identify files where p_dates are wonky:
'''

mxd = arcpy.mapping.MapDocument("CURRENT")
lyrs = arcpy.mapping.ListLayers(mxd)
layers = []

for lyr in lyrs:
    layers.append(str(lyr))

where = """p_date = '0'"""
threshval = 0.5
filename = "D:/Working/p_date_check/p_date_count.txt"
txtFile = open(filename,'a')
pct = 99.99

for layer in layers:
    arcpy.SelectLayerByAttribute_management(layer,"CLEAR_SELECTION","")
    orig_count = int(str(arcpy.GetCount_management(layer)))
    arcpy.SelectLayerByAttribute_management(layer,"NEW_SELECTION",where)
    select_count = int(str(arcpy.GetCount_management(layer)))
    pct = float(float(select_count) / float(orig_count)) * 100
    string_pct = str(pct) + "%"
    txtFile.write("1: " + layer + ", " + string_pct)
    txtFile.write('\n')
    arcpy.SelectLayerByAttribute_management(layer,"CLEAR_SELECTION","")
    
    print "lyuer " + layer + " has been processed: " + string_pct
txtFile.close()
    
