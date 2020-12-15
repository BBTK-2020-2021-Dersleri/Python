def leapYear(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

def dayMonth(month, year):

    if month in [9, 4, 6, 12]:
        print(30)

    elif month in [1, 3, 5, 7, 8,10,11]:
        print(31)        

    elif month == 2 and leapYear(year) == True:
        print(29)

    elif month == 2 and leapYear(year) == False:
        print(28)

    else:
        return None
    
dayMonth(2,2012)  