<VBA> 
'[File Path] is a string that includes a file extension after a "." and can include more than one "." so it will strip off .shp or something like .tar.gz or .shp.xml

Left([FILE_PATH],((InStr([FILE_PATH],".")))-1)