import arcpy
arcpy.env.workspace = r'D:\Geodex.gdb'
subs = arcpy.da.ListSubtypes("Geodex")
for sub in subs:
   arcpy.AssignDomainToField_management("Geodex","MAP_FOR","MAP_FOR",sub)
   arcpy.AssignDomainToField_management("Geodex","MAP_TYPE","MAP_TYPE",sub)
   arcpy.AssignDomainToField_management("Geodex","PRIME_MER","PRIME_MER",sub)
   arcpy.AssignDomainToField_management("Geodex","PROJET","PROJECT",sub)

   