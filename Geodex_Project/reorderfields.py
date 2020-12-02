import arcpy

fc = r'D:\Geodex.gdb\Geodex'
fc1 = r'D:\Geodex.gdb\Geodex1'
fms = arcpy.FieldMappings()

fm_GDX_FILE = arcpy.FieldMap()
fm_GDX_FILE.addInputField(fc,"GDX_FILE")
fms.addFieldMap(fm_GDX_FILE)

fm_GDX_NUM = arcpy.FieldMap()
fm_GDX_NUM.addInputField(fc,"GDX_NUM") 
fms.addFieldMap(fm_GDX_NUM)

fm_GDX_SUB = arcpy.FieldMap()
fm_GDX_SUB.addInputField(fc,"GDX_SUB")
fms.addFieldMap(fm_GDX_SUB)

fm_RECORD = arcpy.FieldMap()
fm_RECORD.addInputField(fc,"RECORD") 
fms.addFieldMap(fm_RECORD)

fm_LOCATION = arcpy.FieldMap()
fm_LOCATION.addInputField(fc,"LOCATION")
fms.addFieldMap(fm_LOCATION)


fm_DATE = arcpy.FieldMap()
fm_DATE.addInputField(fc,"DATE") 
fms.addFieldMap(fm_DATE)


fm_SERIES_TIT = arcpy.FieldMap()
fm_SERIES_TIT.addInputField(fc,"SERIES_TIT")
fms.addFieldMap(fm_SERIES_TIT)


fm_PUBLISHER = arcpy.FieldMap()
fm_PUBLISHER.addInputField(fc,"PUBLISHER") 
fms.addFieldMap(fm_PUBLISHER)

fm_SCALE = arcpy.FieldMap()
fm_SCALE.addInputField(fc,"SCALE") 
fms.addFieldMap(fm_SCALE)

fm_MAP_TYPE = arcpy.FieldMap()
fm_MAP_TYPE.addInputField(fc,"MAP_TYPE") 
fms.addFieldMap(fm_MAP_TYPE)

fm_PRODUCTION = arcpy.FieldMap()
fm_PRODUCTION.addInputField(fc,"PRODUCTION") 
fms.addFieldMap(fm_PRODUCTION)

fm_MAP_FOR = arcpy.FieldMap()
fm_MAP_FOR.addInputField(fc,"MAP_FOR") 
fms.addFieldMap(fm_MAP_FOR)

fm_PROJECT = arcpy.FieldMap()
fm_PROJECT.addInputField(fc,"PROJET") 
fms.addFieldMap(fm_PROJECT)

fm_PRIME_MER = arcpy.FieldMap()
fm_PRIME_MER.addInputField(fc,"PRIME_MER") 
fms.addFieldMap(fm_PRIME_MER)

fm_CATLOC = arcpy.FieldMap()
fm_CATLOC.addInputField(fc,"CATLOC") 
fms.addFieldMap(fm_CATLOC)

fm_HOLD = arcpy.FieldMap()
fm_HOLD.addInputField(fc,"HOLD") 
fms.addFieldMap(fm_HOLD)

fm_YEAR1 = arcpy.FieldMap()
fm_YEAR1.addInputField(fc,"YEAR1") 
fms.addFieldMap(fm_YEAR1)

fm_YEAR1_TYPE = arcpy.FieldMap()
fm_YEAR1_TYPE.addInputField(fc,"YEAR1_TYPE") 
fms.addFieldMap(fm_YEAR1_TYPE)

fm_YEAR2 = arcpy.FieldMap()
fm_YEAR2.addInputField(fc,"YEAR2") 
fms.addFieldMap(fm_YEAR2)

fm_YEAR2_TYPE = arcpy.FieldMap()
fm_YEAR2_TYPE.addInputField(fc,"YEAR2_TYPE") 
fms.addFieldMap(fm_YEAR2_TYPE)

fm_YEAR3 = arcpy.FieldMap()
fm_YEAR3.addInputField(fc,"YEAR3") 
fms.addFieldMap(fm_YEAR3)

fm_YEAR3_TYPE = arcpy.FieldMap()
fm_YEAR3_TYPE.addInputField(fc,"YEAR3_TYPE") 
fms.addFieldMap(fm_YEAR3_TYPE)

fm_YEAR4 = arcpy.FieldMap()
fm_YEAR4.addInputField(fc,"YEAR4") 
fms.addFieldMap(fm_YEAR4)

fm_YEAR4_TYPE = arcpy.FieldMap()
fm_YEAR4_TYPE.addInputField(fc,"YEAR4_TYPE") 
fms.addFieldMap(fm_YEAR4_TYPE)

fm_EDITION_NO = arcpy.FieldMap()
fm_EDITION_NO.addInputField(fc,"EDITION_NO") 
fms.addFieldMap(fm_EDITION_NO)

fm_ISO_TYPE = arcpy.FieldMap()
fm_ISO_TYPE.addInputField(fc,"ISO_TYPE") 
fms.addFieldMap(fm_ISO_TYPE)

fm_ISO_VAL = arcpy.FieldMap()
fm_ISO_VAL.addInputField(fc,"ISO_VAL") 
fms.addFieldMap(fm_ISO_VAL)

fm_LAT_DIMEN = arcpy.FieldMap()
fm_LAT_DIMEN.addInputField(fc,"LAT_DIMEN") 
fms.addFieldMap(fm_LAT_DIMEN)

fm_LON_DIMEN = arcpy.FieldMap()
fm_LON_DIMEN.addInputField(fc,"LON_DIMEN") 
fms.addFieldMap(fm_LON_DIMEN)

fm_X1 = arcpy.FieldMap()
fm_X1.addInputField(fc,"X1") 
fms.addFieldMap(fm_X1)

fm_X2 = arcpy.FieldMap()
fm_X2.addInputField(fc,"X2") 
fms.addFieldMap(fm_X2)

fm_Y1 = arcpy.FieldMap()
fm_Y1.addInputField(fc,"Y1") 
fms.addFieldMap(fm_Y1)

fm_Y2 = arcpy.FieldMap()
fm_Y2.addInputField(fc,"Y2") 
fms.addFieldMap(fm_Y2)

fm_RUN_DATE = arcpy.FieldMap()
fm_RUN_DATE.addInputField(fc,"RUN_DATE") 
fms.addFieldMap(fm_RUN_DATE)

arcpy.Merge_management(fc,fc1,fms)