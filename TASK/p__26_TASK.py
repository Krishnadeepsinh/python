#26. Write a program to calculate total amount after simple interest.
#NAME : KRISHNADEEPSINH
#DATE : 13/1/26

p=int(input("ENTER AMOUNT :"))
r=float(input("Enter rate  :"))
n=float(input("Enter time :"))

amt=(p*r*n)/100

print(f"Interest is : {amt}")
p+=amt
print("FINAL PRINCIPLE AMOUNT IS : ",p)