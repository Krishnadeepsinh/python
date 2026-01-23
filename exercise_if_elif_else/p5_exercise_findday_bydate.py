#5) write a program to findout day of week(monday/tuesday/wednesday) from given date.  
#    https://www.wikihow.com/Calculate-the-Day-of-the-Week

date_day=int(input("ENTER THE INPUT FOR DAY : "))
month=int(input("ENTER THE INPUT FOR MONTH  : "))

year=26-0
reminder_of_year=year//4  
year+=reminder_of_year
year+=6
lis=["",0,3,3,6,1,4,6,2,5,0,3,5] #value of table according to calender
days=["Sunday","Monday","Tuesday","Wednesday","Thrsday","Friday","Sunday"] #days of week
result= year+lis[month]+date_day
result%=7
print(days[result])
