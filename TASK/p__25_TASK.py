#25. Write a program to calculate simple interest using principal, rate, and time.
#NAME : KRISHNADEEPSINH
#DATE : 12/1/26

p=int(input("ENTER AMOUNT :"))
r=float(input("Enter rate  :"))
n=float(input("Enter time :"))

amt=(p*r*n)/100
print(f"Interest is : {amt}")