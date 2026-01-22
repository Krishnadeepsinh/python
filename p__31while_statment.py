# write a program to print given amount into words
# input : 12345 output : one two three four five 
words = ['zero','one','two','three','four','five','six','seven','eight','nine']

no=int(input("ENTER THE AMOUNT : "))
list=[]
while no>0:
    reminder=no%10
    list.insert(0,words[reminder])
    no=no//10
print(' '.join(list))
    