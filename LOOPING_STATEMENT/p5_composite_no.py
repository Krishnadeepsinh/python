'''
write a program to figure out whether given number is composite number or not 
'''
import sys
number=int(input("ENTER THE NUMBER : "))
divisor=2
remider=0  
while divisor<number:   
        remider=number%divisor
        if remider==0:
          print(f"THE NO : {number} IS COMPOSITE NUMBER  ")
          sys.exit(1)
        else:
            divisor+=1
  
print(f"THE NO : {number} IS NOT COMOSITE  NUMBER ")