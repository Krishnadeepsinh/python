import shutil as s
width=s.get_terminal_size().columns
# 1	 Without return value without argument
def getprintline():
    print('_'*width)

# 2	Without return value with argument 
def printmessage(msg):
    print(msg.center(width))

# 3	 With return value without argument
def pi():
    pi=22/7
    return pi 

getprintline()
printmessage("KRISHNADEEPSINH")
getprintline()
pi=pi()

print('pi=',pi)
