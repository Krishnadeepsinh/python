#6) write a program to convert all negative values into positive values in the same list 


list = [12, -45, 7, -3, 89, -22, 0, 34, -9, 56]
print(f"OLD LIST IS = {list}")
for val in list:
    if val<0:
        list[list.index(val)]=val*-1

print(f"NEW LIST IS = {list}")
