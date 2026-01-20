# 2) write a program to accept length and width of two different farm from user. and find out & display which farm is bigger 
#NAME : KRISHNADEEPSINH
#DATE :20/1/26

farm1_length=float(input("ENTER THE LENGTH OF FARM 1 : "))
farm1_width=float(input("ENTER THE WIDTH OF FARM 1 : "))

farm2_length=float(input("ENTER THE LENGTH OF FARM 2 : "))
farm2_width=float(input("ENTER THE WIDTH OF FARM 2 : "))

farm1_area = farm1_length * farm1_width
farm2_area = farm2_length * farm2_width

if farm1_area == farm2_area:
    print("BOTH FARM ARE EQUAL")

if farm1_area > farm2_area:
    print("FARM 1 IS BIGGER ")

if farm1_area < farm2_area:
    print("FARM 2 IS BIGGER ")
    