fc= 'Geodex'


rows = arcpy.UpdateCursor(fc,"","","","GDX_FILE,RECORD,DATE D,YEAR2 D")

i = 0
file2 = 0

for row in rows:
    file = row.getValue("GDX_FILE")
    if file == file2:
        i += 1
        id = str(file) + "." + str(i)
    else:
        i = 0
        id = str(file) + "." + str(i)
        i += 1
        file2 = row.getValue("GDX_FILE")

    row.setValue("GDXID",id)
    rows.updateRow(row)
    string = id
    print string

del rows, row        
        