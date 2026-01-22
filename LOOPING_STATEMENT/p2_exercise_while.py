# write a program to print following series
#2)   1    8   27   125  ....... 1000

no=1
cube=0
reminder=0
while cube<961:
    cube=no*no*no
    reminder=no%2
    print(cube,end='  ')
    no+=1
