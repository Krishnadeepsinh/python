'''
Docstring for p__4_pattern_making

5 4 3 2 1
5 4 3 2
5 4 3
5 4
5

'''
for row in range(6,1,-1):
    count=5
    for num in range(1,row):
        print(count,end=" ")
        count-=1
    print(" ")

