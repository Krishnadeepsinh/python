# write a program to find out whether given shape is square or portrait or landscape using user given length and width 
#NAME:KRISHNADEEPSINH
#DATE:19/1/26

length=int(input("ENTER THE LENGTH : "))
width=int(input("ENTER THE WIDTH : "))

#if the shape is square 
if length==width:
    print("THE SHAPE IS SQUARE ")

#if the shape is potrait
if length>width:
    print("THE SHAPE IS PORTRAIT")

#if the shape is landscape
if length<width:
    print("THE SHAPE IS LANDSCAPE")
  