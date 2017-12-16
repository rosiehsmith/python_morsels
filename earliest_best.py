def get_earliest(date1, date2):
    month1, day1, year1 = date1.split('/')
    month2, day2, year2 = date2.split('/')

    fullDate1 = year1 + month1 + day1
    fullDate2 = year2 + month2 + day2

    if(year1, month1, day1) > (year2, month2, day2):
        return date2
    return date1

    #tuple unpacking is amazing!!!!
    #comparing tuples is awesome!