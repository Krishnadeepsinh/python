#2) write a program to accept 2 number from user. and accept choice for operations.
#operations will be addition, subtraction, multiplication, division
#do operation and display result as per user choice about operation using if elif else statements.

no1=int(input("ENTER NO1 :"))
no2=int(input("ENTER NO2 :"))

print("""1 FOR ADDITION 
         2 FOR SUBTRACTION
         3 FOR MULTIPILICATION
         4 FOR DIVISON
""")
ch=int(input("ENTER THE CHOICE FOR OPERATIONS :"))
if ch==1:
    print(f"ADDITON OF {no1} + {no2}={no1+no2}")
elif ch==2:
    print(f"SUBTRACTION OF {no1} - {no2}={no1-no2}")
elif ch==3:
    print(f"MULTIPICATION OF {no1} * {no2}={no1*no2}")
elif ch==4:
    print(f"DIVISION OF {no1} / {no2}={no1/no2}")
else:
    print("INVAILD INPUT")
