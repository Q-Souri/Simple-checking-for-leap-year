def check_leap(year):
    if ((year % 4 == 0)or
    (year %100 != 0) and
    (year %4 == 0)):
        print("Given year is a leap year")
    else:
        print("Given year is not a leap year!")

year = int(input("Enter the number: "))

check_leap(year)

    
    


    
