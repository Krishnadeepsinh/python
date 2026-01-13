#37. Write a program to calculate discount amount using price and discount rate.
#NAME : KRISHNADEEPSINH
#DATE : 13/1/26


dic={'RAM':15000,'SSD':5500,'MOTHERBOARD':8000,'GTX1650_GPU':7500,'peripherials':3500}
dis=float(input("ENTER THE PERCENTAGE FOR DISCOUNT : "))
final=list(dic.values())
amt_final=sum(final)
amt_final=amt_final-amt_final*dis/100
print(amt_final)