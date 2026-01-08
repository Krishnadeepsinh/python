#WAP PROGRAM TO CONVERT USER INPUT NUMBER INTO STRING 
#EX:10 TO ONE ZERO
#DATE:8/1/2026

no=input("ENTER NUMBER :")
#convert amount into integer
no=int(no)
first=no//10
last=no%10

words = ['zero','one','two','three','four','five','six','seven','eight','nine']
#           0     1     2      3       4      5     6       7       8       9

print(words[first],words[last])