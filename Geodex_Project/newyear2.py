yearfields = ["approx_dat", "pub_date", "comp_date", "base_date", "field_chec", "image_year", "photo_2", "photo_insp", "image_date", "prelim_edi", "cmp_fr", "interim_ed", "printed", "printed_ci", "revised", "site_surve", "transport", "prov_editi", "mg_dcl", "photo_revi", "edition_of", "reprint"]
newfields = []
for field in yearfields:
    name = field + "_s"
    arcpy.AddField_management("Geodex",name,"SHORT")