'''
Docstring for p__2_pattern_making

1
0 1
0 1 0
1 0 1 0
1 0 1 0 1

'''
count=1

for row in range(1,6):
    for num in range(1,row+1):
        print(count,end=' ')
        if count==1:
            count=0
        else:
            count=1
            
    print(" ")