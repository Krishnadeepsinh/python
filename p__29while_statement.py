# write a program to print following series 
# 1     3       5       7       9       11      13      .... 100

no_entry=1
no_close=int(input("ENTER SERIES ENDING NUMBER  : "))
while no_entry<=no_close: 
    print(no_entry,end=' ')
    no_entry+=2