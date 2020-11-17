year = int(input("Enter a year: "))  
if (year % 4) == 0:  
    if (year % 100) == 0:  
        if (year % 400) == 0:
            print("{} is a leap year".format(year))
        else:
            print("{} is not a leap year".format(year)) 
    else:
        print("{} is a leap year".format(year))
            
else:
    print("{} is not a leap year".format(year)) 