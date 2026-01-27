#2) write a program to generate and display sum of all the float values in tuple and also calculate average 

tuple1 = (1.0, 2.5, 3.14, 4.2, 5.0, 6.7, 7.8, 8.9, 9.1, 10.0)
sum=0
count=0
for item in tuple1:
    sum+=item
    count+=1

print(f"sum of tuple values is {sum}")

print(f"average of tuple is {sum/count} ")