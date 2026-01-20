# 3) write a program to accept day of week (between 1 to 7) and then #display name of day. (use simple if decision making)
#            input 1 : monday 
#            input 2 : tuesday 
#            input 7 : sunday 

day=int((input("ENTER THE WEEK DAY NO: ")))
if day==1:
    print(f"{day} MONDAY")
if day==2:
    print(f"{day} TUESDAY")
if day==3:
    print(f"{day} WEDNESDAY")
if day==4:
    print(f"{day} THURSDAY")
if day==5:
    print(f"{day} FRIDAY")
if day==6:
    print(f"{day} SATURDAY")
if day==7:
    print(f"{day} SUNDAY")