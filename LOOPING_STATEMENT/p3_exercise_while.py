# write a program to print following series
#3)   1    -8   27  -64  .....    1000

no=1
cube=0
reminder=0
while no<11:
    cube=no*no*no
    reminder=no%2
    if no%2==0:
       cube=0-cube
    print(cube,end='  ')
    no+=1
