#for loop with string
# count vowels  
string=input("ENTER VALUE / NAME : ")
vowels=['a','e','i','o','u','A','E','I','O','U']
count=0
for letter in string:
        if letter in vowels:
                count+=1
print(count)