#4) write a program to count digits in given string 
count=0
str=input("ENTER THE ALPHA NUMERIC : ")
for no in str:
    if no in ['1','2','3','4','5','6','7','8','9','0']:
       count+=1
print(count) 