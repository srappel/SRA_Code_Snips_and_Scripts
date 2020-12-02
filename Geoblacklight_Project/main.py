import os
from os import path
import json
import datetime
from datetime import date, time, timedelta
import time
import csv

# read through the csv file that contains all the metadata
rawContent = open("allinone.csv", 'r')
reader = csv.reader(rawContent)
metadatalist = list(reader)
#L = len(metadatalist)

#create a csv file that contains headers of GeoBlacklight elements, and add each record retrieved from a 2-D Matrix transferred from All_in_onetest.csv
with open("metadatasheet.csv", 'w') as csvfile:
	fieldnames = ['uuid','dc_identifier_s','dc_title_s','dc_description_s','dc_rights_s','dct_provenance_s','dct_references_s','layer_id_s','layer_geom_type_s','layer_modified_dt','layer_slug_s','georss_box_s','dc_creator_sm','dc_format_s','dc_language_s','dc_publisher_s','dc_relation_s','dc_subject_sm','dc_type_s','dct_spatial_sm','dct_temporal_sm','dct_issued_s','dct_isPartOf_s','georss_point_s','georss_polygon_s','solr_pt','solr_bbox','solr_geom','solr_jts','solr_ne_pt','solr_we_pt','solr_issued_dt','solr_year_i','solr_wcs_url','solr_wfs_url','solr_wms_url']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	
	
	#iterate through the metadata matrix and write them into a csv file
	for i in metadatalist:
		L = metadatalist.index(i)
		accessCons = str(metadatalist[L][23])
		if accessCons == 'None':
			rights = 'Public'
		else:
			rights = 'Restricted'
			
		writer.writerow({'uuid': metadatalist[L][0],'dc_identifier_s': metadatalist[L][0],'dc_title_s': metadatalist[L][1],'dc_description_s': metadatalist[L][2],'dc_rights_s': rights,'dct_provenance_s': metadatalist[L][3],'dct_references_s': ' ','layer_id_s': ' ','layer_geom_type_s': '','layer_modified_dt':datetime.datetime.fromtimestamp(path.getmtime("test.csv")),'layer_slug_s': ' ','georss_box_s': '','dc_creator_sm': '','dc_format_s': metadatalist[L][8],'dc_language_s': '','dc_publisher_s': '','dc_relation_s': ' ','dc_subject_sm': ' ','dc_type_s': '','dct_spatial_sm': '','dct_temporal_sm': metadatalist[L][6],'dct_issued_s': metadatalist[L][6],'dct_isPartOf_s': ' ','georss_point_s': '','georss_polygon_s': ' ','solr_pt': ' ','solr_bbox': ' ','solr_geom': '','solr_jts': ' ','solr_ne_pt': ' ','solr_we_pt': ' ','solr_issued_dt': ' ','solr_year_i': ' ','solr_wcs_url': ' ','solr_wfs_url': ' ','solr_wms_url': ' '})
		
		#elimiate the colon from the text and retrieve the content after the colon
		newList = []
		for e in metadatalist[L]:
			if ":" in str(e):   #check to see if the element of the list contains ':', if yes, split and put into a new list, if no, put into the new list right away
				subList = [e.split(':')]
				newList.append(str(subList[0][-1]).strip())
			else: 
				newList.append(e)
		#print newList
		
		# create multiple .js files at one time along with the csv file
		newFile = open(str(L) + '.js', 'w')
		y = json.dumps({
		  "uuid": metadatalist[L][0],
		  "dc_identifier_s": metadatalist[L][0],
		  "dc_title_s": newList[1],
		  "dc_description_s": newList[2],
		  "dc_rights_s": rights, #if "'none'" return 'Public' elif "'uwm'" return 'restricted',
		  "dct_provenance_s": newList[3],
		  "dct_references_s": " ",
		  "layer_id_s": " ",
		  "layer_geom_type_s": " ",
		  "layer_modified_dt": str(datetime.datetime.fromtimestamp(path.getmtime("metadatasheet.csv"))), #read last modified time of json file created(find corresponding function)
		  "layer_slug_s": " ",
		  "georss_box_s": "",
		  "dc_creator_sm": "",
		  "dc_format_s": newList[8],
		  "dc_language_s": "",
		  "dc_publisher_s": "",
		  "dc_relation_s": " ",
		  "dc_subject_sm": " ", #can have multiple varibles 
		  "dc_type_s": "",
		  "dct_spatial_sm": "",
		  "dct_temporal_sm": newList[6],
		  "dct_issued_s": newList[6],
		  "dct_isPartOf_s": " ",
		  "georss_point_s": "",
		  "georss_polygon_s": " ",
		  "solr_pt": " ",
		  "solr_bbox": " ",
		  "solr_geom": "",
		  "solr_jts": " ",
		  "solr_ne_pt": " ",
		  "solr_we_pt": " ",
		  "solr_issued_dt": " ",
		  "solr_year_i": " ",
		  "solr_wcs_url": " ",
		  "solr_wfs_url": " ",
		  "solr_wms_url": " ",
		}, sort_keys=True, indent=4, separators=(',',':'))
		z = str(y)
		newFile.write(y)
		newFile.close()
raw_input()

