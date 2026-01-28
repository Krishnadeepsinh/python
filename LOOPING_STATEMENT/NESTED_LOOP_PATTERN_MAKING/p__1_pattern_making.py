'''
Docstring for p__1_pattern_making

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

'''

for row in range(1,6):
    for num in range(1,row+1):
        print(num,end=' ')
    print(" ")