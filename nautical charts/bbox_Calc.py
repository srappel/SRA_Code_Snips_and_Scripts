############################
    ##### From the 034 field ###
    ############################

    # The float versions of the extents are rounded to 8 decimal points.  That's a precision of just over 1mm at the equator.

    #Find the index for 034:
    i = almaData[0].index('034')

    ## scale
    scaleRegex = re.compile(r'(\$b\s)(\d*)')
    scaleMO = scaleRegex.search(row[i])
    if not scaleMO is None:
        scale = int(scaleMO[2])
    else:
        scale = None
        
    rowDict['scale'] = scale

    ## north    
    #Get Southernmost Extent
    southRegex = re.compile(r'(\$g\s)(\D)(\d{3})(\d{2})(\d*)')
    southMO = southRegex.search(row[i])
    if not southMO is None:
        southDMS = {
            'dir':southMO[2],
            'd':int(southMO[3]),
            'm':int(southMO[4]),
            's':float(southMO[5])
        }
        north = DMS2DD(southDMS)
    else:
        north = None
    if not north is None:
        north = round(north, 8)    
    
    rowDict['north'] = north

    ## south
    #Get Northernmost Extent
    northRegex = re.compile(r'(\$f\s)(\D)(\d{3})(\d{2})(\d*)')
    northMO = northRegex.search(row[i])
    if not northMO is None:
        northDMS = {
            'dir':northMO[2],
            'd':int(northMO[3]),
            'm':int(northMO[4]),
            's':float(northMO[5])
        }
        south = DMS2DD(northDMS)
    else:
        south = None

    if not south is None:
        south = round(south, 8)
    
    rowDict['south'] = south
    
    ## west
    #Get westernmost Extent
    westRegex = re.compile(r'(\$d\s)(\D)(\d{3})(\d{2})(\d*)')
    westMO = westRegex.search(row[i])
    if not westMO is None:
        westDMS = {
            'dir':westMO[2],
            'd':int(westMO[3]),
            'm':int(westMO[4]),
            's':float(westMO[5])
        }
        west = DMS2DD(westDMS)
    else:
        west = None

    if not west is None:
        west = round(west, 8)
    
    rowDict['west'] = west
    
    ## east
    #Get easternmost Extent
    eastRegex = re.compile(r'(\$e\s)(\D)(\d{3})(\d{2})(\d*)')
    eastMO = eastRegex.search(row[i])
    if not eastMO is None:
        eastDMS = {
            'dir':eastMO[2],
            'd':int(eastMO[3]),
            'm':int(eastMO[4]),
            's':float(eastMO[5])
        }
        east = DMS2DD(eastDMS)
    else:
        east = None
    
    if not east is None:
        east = round(east, 8)    
    
    rowDict['east'] = east    