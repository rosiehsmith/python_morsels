def get_earliest(date1, date2):
    splitDate1 = date1.split('/')
    splitDate2 = date2.split('/')
    
    month1, month2 = splitDate1[0], splitDate2[0]
    day1, day2 = splitDate1[1], splitDate2[1]
    year1, year2 = splitDate1[2], splitDate2[2]

    if(year1 > year2):
        return date2
    else:
        if(month1 > month2):
            return date2
        elif(month1 == month2):
            if(day1 > day2):
                return date2
            else:
                return date1
        else:
            return date1