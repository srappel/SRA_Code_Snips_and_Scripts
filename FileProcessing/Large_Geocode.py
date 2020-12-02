#import system modules
import arcpy
import csv
from arcpy import env
env.workspace = r'H:\Departments\AGSL\GIS\Patrons\2018_06\Erik_Gunn'

#Set Constant Variables:
address_locator = r'H:\Departments\AGSL\GIS\Patrons\2018_06\Erik_Gunn\mke_street_locator'

#Loop through CSV
tables = arcpy.ListTables()

for t in tables:
	address_table = t
	table_string = str(t)
	year_string = table_string[:4]
	geocode_result = str(env.workspace) + '\\' + year_string + '\\' + 'geocode_result.shp'
	
	arcpy.GeocodeAddresses_geocoding(address_table, address_locator, "'Full Address' LOCATION", geocode_result, 'STATIC')
	print geocode_result + ' has completed sucessfully'
