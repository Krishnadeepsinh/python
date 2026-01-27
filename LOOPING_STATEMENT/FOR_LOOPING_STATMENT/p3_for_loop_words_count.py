#3) write a program to count words in given string 
count=1
str=input("ENTER THE NAME : ")
for val in str:
    if val==' ':
        count+=1
    
print(f"NAME HAS LENGTH OF WORDS ARE {count}")