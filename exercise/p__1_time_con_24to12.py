 '''1) write a program to convert 24 hours time into 12 hours format time and display it with AM PM message. 
        input : 15 hours 
        output  3 PM 

        input : 11 hours 
        output  11 AM 

        input : 25 hours 
        output  invalid input '''

#NAME:KRISHNADEEPSINH
#DATE:19/1/26

time=int(input("ENTER THE TIME IN HOUR FROM 1 TO 24 : "))
am='am'
pm='pm'

if time<=12:
       print("TIME IN HOURS IS : ",time," ",am)
if time>12 and time<=24:
       print("TIME IN HOURS IS : ",time-12," ",pm)
if time>24:
       print('INVAILD TIME ')
       