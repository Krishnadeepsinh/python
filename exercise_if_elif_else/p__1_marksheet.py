'''
1) 
Write a program that takes a 5 subject marks from user. calculate total and Percentage  and prints the grade using the following conditions:

| Percentage | Grade |
| ---------- | ----- |
| 90–100     | A+    |
| 80–89      | A     |
| 70–79      | B     |
| 60–69      | C     |
| 50–59      | D     |
| below 50   | Need to improve  |
---------------------------------------
'''

s1=int(input("ENTER THE SUBJECT 1 MARK : "))
s2=int(input("ENTER THE SUBJECT 2 MARK : "))
s3=int(input("ENTER THE SUBJECT 3 MARK : "))
s4=int(input("ENTER THE SUBJECT 4 MARK : "))
s5=int(input("ENTER THE SUBJECT 5 MARK : "))

total_marks=s1+s2+s3+s4+s5
percentage=total_marks/5

if percentage>=90 and percentage<=100:
    print("OBTAINED A+ GRADE")
elif percentage>=80 and percentage<=89:
    print("OBTAINED A GRADE")
elif percentage>=70 and percentage<=79:
    print("OBTAINED B GRADE")
elif percentage>=60 and percentage<=69:
    print("OBTAINED C GRADE")
elif percentage>=50 and percentage<=59:
    print("OBTAINED D GRADE")
else:
    print("Need to improve")