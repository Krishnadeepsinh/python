#5) write a program to count vowels, consonants, digits, words, and symbol in given list 

string=input("ENTER STRINGS : ")
digit=['1','2','3','4','5','6','7','8','9','0']
vowels=['a','e','i','o','u','A','E','I','O','U']
consonants = [ 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm','n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
v=0
c=0
d=0
s=0
for char in string:
    if char in digit:
        d+=1
    elif char.lower() in vowels:
        v+=1
    elif char.lower() in consonants:
        c+=1
    else:
        s+=1

print('NO OF WORDS ARE : ',len(string.split()))
print(f"NO OF DIGITS ARE : {d} ")
print(f"NO OF VOWELS ARE :  {v} ")
print(f"NO OF CONSONANTS ARE : {c} ")
print(f"NO OF SYMBOLS ARE : {s} ")