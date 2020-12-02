import operator

yearfields = ["approx_dat", "pub_date", "comp_date", "base_date", "field_chec", "image_year", "photo_2", "photo_insp", "image_date", "prelim_edi", "cmp_fr", "interim_ed", "printed", "printed_ci", "revised", "site_surve", "transport", "prov_editi", "mg_dcl", "photo_revi", "edition_of", "reprint"]
yearfields_s = []
for year in yearfields:
    newyear = year + "_s"
    yearfields_s.append(newyear)

rows = arcpy.UpdateCursor("Geodex")

for row in rows:
    
    approx_dat = row.getValue("approx_dat_s")
    pub_date = row.getValue("pub_date_s")
    comp_date = row.getValue("comp_date_s")
    base_date = row.getValue("base_date_s")
    field_chec = row.getValue("field_chec_s")
    image_year = row.getValue("image_year_s")
    photo_2 = row.getValue("photo_2_s")
    photo_insp = row.getValue("photo_insp_s")
    image_date = row.getValue("image_date_s")
    prelim_edi = row.getValue("prelim_edi_s")
    cmp_fr = row.getValue("cmp_fr_s")
    interim_ed = row.getValue("interim_ed_s")
    printed = row.getValue("printed_s")
    printed_ci = row.getValue("printed_ci_s")
    revised = row.getValue("revised_s")
    site_surve = row.getValue("site_surve_s")
    transport = row.getValue("transport_s")
    prov_editi = row.getValue("Prov_editi_s")
    mg_dcl = row.getValue("mg_dcl_s")
    photo_revi = row.getValue("photo_revi_s")
    edition_of = row.getValue("edition_of_s")
    reprint = row.getValue("reprint_s")
    values = [approx_dat,pub_date,comp_date,base_date,field_chec,image_year,photo_2,photo_insp,
              image_date,prelim_edi,cmp_fr,interim_ed,printed,printed_ci,revised,site_surve,
              transport,prov_editi,mg_dcl,photo_revi,edition_of,reprint]

    dict = {}
    
    i = 0
    while i <= 21:
        dict[yearfields_s[i]] = values[i]
        i += 1

    sorted_dict = sorted(dict.items(), key=operator.itemgetter(1))

    tuple1 = sorted_dict[-1]
    value1 = tuple1[1]
    type1 = tuple1[0]
    row.setValue("YEAR1",value1)
    row.setValue("YEAR1_TYPE_t",type1)

    tuple2 = sorted_dict[-2]
    value2 = tuple2[1]
    type2 = tuple2[0]
    row.setValue("YEAR2",value2)
    row.setValue("YEAR2_TYPE_t",type2)

    tuple3 = sorted_dict[-3]
    value3 = tuple3[1]
    type3 = tuple3[0]
    row.setValue("YEAR3",value2)
    row.setValue("YEAR3_TYPE_t",type3)    

    tuple4 = sorted_dict[-4]
    value4 = tuple4[1]
    type4 = tuple4[0]
    row.setValue("YEAR4",value4)
    row.setValue("YEAR4_TYPE_t",type4)

    rows.updateRow(row)

del row
del rows


rows = arcpy.UpdateCursor("Geodex")



ofcs = [97,98, 99, 100, 102, 103, 104, 105, 106, 108, 109, 110, 112, 113, 114, 115, 116, 118, 119, 120, 121, 122]
ofc_dict = {}

i = 0
while i <= 21:
    ofc_dict[yearfields_s[i]] = ofcs[i]
    i += 1

for row in rows:
    years = ["YEAR1","YEAR2","YEAR3","YEAR4"]
    for year in years:
        tofield = year + "_TYPE"
        fromfield = year + "_TYPE_t"
        key = row.getValue(fromfield)
        value = ofc_dict[key]    
        row.setValue(tofield,value)
        rows.updateRow(row)
        newval = row.getValue(year)
        if newval == None:
            row.setValue(tofield, None)
            row.setValue(fromfield, None)
            rows.updateRow(row)

del row
del rows




    

    
    
     