#write a program to create function that calculate and return simple interest of given amount rate and year 

def getsimpleinterest(p,r,n):
    return p*r*n/100
 
p=int(input("ENTER THE PRINCIPLE AMOUNT : "))
r=float(input("ENTER THE RATE OF INTEREST : "))
n=int(input("ENTER THE TIME : "))

res=getsimpleinterest(p,r,n)
print(f"SIMPLE INTEREST IS : {res}")