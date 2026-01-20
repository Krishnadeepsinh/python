'''
3 write a program to accept month number from user and display how many days month has. (use logical operator or)
    input : 1 output : this month has 31 days 
    input : 4 output : this month has 30 days 
'''
month_no=int(input("ENTER THE MONTH NUMBER : "))

if month_no==1 or month_no==3 or month_no==5 or month_no==7 or month_no==8 or month_no==10 or month_no==12:
    print(f"THE MONTH NO {month_no} HAS 31 DAYS")
elif month_no==4 or month_no==6 or month_no==9 or month_no==11  :
    print(f"THE MONTH NO {month_no} HAS 30 DAYS")
else:
    print(f"THE MONTH NO {month_no} HAS 28 OR 29 DAYS")