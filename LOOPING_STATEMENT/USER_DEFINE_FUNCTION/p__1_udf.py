#write a program to create function that convert given fahrenheit into celsius 

def getcelsius(f):
    #(32°F − 32) × 0.5555555555555556 = C
    return f-32*0.5555555555555556



print(f"CELSIUS IS : {getcelsius(float(input("ENTER THE FAHRNEHIET : ") ))}")