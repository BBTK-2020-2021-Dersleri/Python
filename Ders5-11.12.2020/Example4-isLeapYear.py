year = int(input("Enter a year: "))  
def isLeapYear(year):
    if (year % 4) == 0:  
        if (year % 100) == 0:  
            if (year % 400) == 0:  
                return True  
            else:  
                return False  
        else:  
            return True  
    else:
        return False

if(isLeapYear(year)):
    print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))