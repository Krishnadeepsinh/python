# concept of user defined function
#syntax 
#def function-name(parameters):
#example 




def getSquare(number): 
    square= number * number
    return square

def getCube(num):
    return getSquare(num) * num


n1 = int(input("ENTER NUMBER TO FIND SQAURE & CUBE : "))
result=getSquare(n1)
print(f"CUBE OF {n1} IS : {result}")

result1=getCube(n1)

print(f"CUBE OF {n1} IS : {result1}")


