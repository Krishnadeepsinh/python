'''
write a program to figure out whether given number is prime number or not 
'''
import sys
number=int(input("ENTER THE NUMBER : "))
divisor=2
remider=0
if number!=2 and number%2==0:
    print(f"THE NO : {number} IS NOT PRIME ")
    sys.exit(1)
else:
    while divisor<number:   
        remider=number%divisor
        if remider==0:
          print(f"THE NO : {number} IS NOT PRIME ")
          sys.exit(1)
        else:
            divisor+=1
    print(f"THE NO : {number} IS PRIME NUMBER ")