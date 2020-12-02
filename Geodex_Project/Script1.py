if photo2 IS NOT NULL:
    if photo2 > sitesur AND photo2 > rev AND photo2 > print AND photo2 > phoins:
        DATE = photo2
    elif sitesur > photo2 AND sitesur > rev AND sitesur > print AND sitesur > phoins:
        DATE = photo2

And so on...


or make an array dates = []
populate the array with the values
sort the values descending
date = dates[0]
