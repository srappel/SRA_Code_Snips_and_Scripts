import os
import arcpy

#path to the text file containing readme records
tfile = "D:/Metadata/all_samp.txt"

#path to an output text file
ofile = "D:/Metadata/ofile.txt"
outtxt = open(ofile,'w')

#open the text file as "file"
with open(tfile,'r') as file:
    #iteratres through lines
    lines = file.readlines()
    

    for line in lines:
        #searches for the string on each line
        if "digital - R:" in line:
            #strips the "digital - " from the line leaving only the path
            path = line.lstrip("digital - ").rstrip()
            #path2 = path.replace('\\','\\\\')
            writestring = path + ": "
            outtxt.write(writestring + '\n')
            features = []

            #Walks through the path defined on the line and finds all "FeatureClass" files.                        
            for dirpath, dirnames, filenames in arcpy.da.Walk(path,datatype="FeatureClass"):
                #adds the complete file path string to a list "features"
                for filename in filenames:
                    features.append(os.path.join(dirpath, filename))
                                        
            for fc in features:
                #print fc
                #each "fc" is a feature

                #"Describe" the feature                
                desc = arcpy.Describe(fc)

                #Get the features patial reference.
                #This will vary from fc to fc, but it's important to know it.
                sr = desc.spatialReference

                #get the extents, note that these values will be in the original sr defined above                
                XMAX = desc.extent.XMax
                XMIN = desc.extent.XMin
                YMAX = desc.extent.YMax
                YMIN = desc.extent.YMin

                #create an in memory polygon
                pnt1 = arcpy.Point(XMIN, YMIN)
                pnt2 = arcpy.Point(XMIN, YMAX)
                pnt3 = arcpy.Point(XMAX, YMAX)
                pnt4 = arcpy.Point(XMAX, YMIN)
                array = arcpy.Array()
                array.add(pnt1)
                array.add(pnt2)
                array.add(pnt3)
                array.add(pnt4)
                array.add(pnt1)
                polygon = arcpy.Polygon(array, sr)
                #see? that's where we used the spatial reference ^^
                #If you don't include this, it wont let you project the polygon to anything else!

                #sr2 is a spatial reference object, here it is set to "WGS84" which has a "factory code" 4326
                #WGS84 will give us latitude and longtitude decimal degrees that we're looking for.
                sr2 = arcpy.SpatialReference(4326)

                #reproject the polygon as wgs84                
                polygon2 = polygon.projectAs(sr2)

                #get the extent of the selected polygon
                #NOTE: arcpy.describe.extent is for feature classes.
                #Here we just need the extent property of the polygon we created.
                extent = polygon2.extent

                #the four extents of the projected polygon.JSON
                #we want these as strings, hence str()
                x1 = str(extent.XMax)
                x2 = str(extent.XMin)
                y1 = str(extent.YMax)
                y2 = str(extent.YMin)

                #ENVELOPE(W, E, N, S) (solr_geom)
                #SWNE (georss box)
                fcstring = fc + ": " + "ENVELOPE(" + x2 + ", " + x1 + ", " + y1 + ", " + y2 + ") " + y2 + " " + x2 + " " + y1 + " " + x1
                outtxt.write(fcstring + '\n')
                #So we're writing them to a text file here, but you could continue to use these,
                #just remember that x1, x2, y1, and y2 are strings for east, west, north, and south
                #values in decimal degrees.

            #This just adds an extra line to separate out the next folder of features    
            outtxt.write('\n')
                           
#gotta close the text files to release locks...
outtxt.close()
file.close()



                
         
                
                
            
                

            

            

        
