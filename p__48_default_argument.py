#default argument function
# write a program that will return total inches of given meter, foot, inches 
def getinches(meter,foot=0,inches=0):
    print(f'meter = {meter}  foot = {foot}  inches = {inches}')
    total=meter*39.37
    total = total + (foot * 12) + inches
    return total

print(getinches(10,5,7))
print(getinches(10,5))
print(getinches(10))