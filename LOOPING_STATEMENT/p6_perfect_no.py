#6 write a program to figure out whether given number  is perfect number or not

number=int(input("ENTER THE NUMBER : "))

sum=1
divisor=2
remider=0  
while divisor<number:   
        remider=number%divisor
        if remider==0:
          sum+=divisor
          divisor+=1
        else:
            divisor+=1
  
if(sum==number):
    print(f"THE NO : {number} IS PERFECT NUMBER ")
else:
    print(f"THE NO : {number} IS NOT PERFECT NUMBER ")
