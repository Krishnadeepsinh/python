#7) write a program to figure out whether given number  is armstrong number or not

no=int(input("ENTER THE NUMBER : "))
no1=no
sum=0
count=len(str(no1))

while no1>0:
    remider=no1%10
    sum+=pow(remider,count)
    no1=no1//10

if sum==no:
    print(f"THE {no} IS ARMSTRONG NUMBER ")
else:
    print(f"THE {no} IS NOT ARMSTRONG NUMBER ")