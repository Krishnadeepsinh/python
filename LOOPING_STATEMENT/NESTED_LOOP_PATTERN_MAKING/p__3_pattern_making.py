'''
Docstring for p__2_pattern_making

1 2 3 4 5  
1 2 3 4  
1 2 3  
1 2  
1
'''

for row in range(6,1,-1):
    for num in range(1,row ):
        print(num,end=' ')
    print(" ")