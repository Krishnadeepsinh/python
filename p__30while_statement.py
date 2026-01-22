# write a program to print following series 
# 1     -4      9     -16     25      -36     1000
   

no=1
sq=0
reminder=0
while sq<961:
    sq=no*no
    reminder=no%2
    if no%2==0:
        sq=0-sq
    print(sq,end='  ')
    no+=1
