'''
Docstring for p__5_pattern_making

* * * * *
 * * * *
  * * *
   * *
    *
    *
   * *
  * * *
 * * * *
* * * * *

'''

astrek=6
sp=0

for row in range(1,6):
    for sp1 in range (1,sp+1):
        print(" ",end="")
    for col in range(1,astrek):
        print("*",end=" ")
    astrek-=1
    sp+=1
    print("")

astrek=1
sp=4
for row in range(1,6):
    for sp1 in range(1,sp+1):
        print("",end=" ")
    for col in range(1,astrek+1):
        print("*",end=" ")
    astrek+=1
    sp-=1
    print("")