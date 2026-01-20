#4) write a program to find out whether given year is millennium year or #not. using if else decision making statements.

year=int(input("ENTER THE YEAR : "))

if (year%1000==0):
    print("YEAR IS MILLENNIUM ",year)
else:
    print("YEAR IS NOT MILLENNIUM ",year)