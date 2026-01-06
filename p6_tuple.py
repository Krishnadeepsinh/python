#WAP TO CREATE A TUPLE & PERFORM VAROIUS PRINT TASK ON IT 
#NAME=KRISHNADEEPSINH
#DATE=6/1/2026

nation=('INDIA','RUSSIA','UNITED STATE','CHINA','GERMANY','JAPAN')
boxes=(100,'BHAVNAGAR',True,None,3.14)

#print tuple 
print(nation)
print(boxes)

#print specfic index
print(nation[0])
print(boxes[0])


#print tuple in specfic range of 

print(nation[1:5])
print(boxes[1:3])

#print from specfic index to end of tuple

print(nation[2:])
print(boxes[3:])

#find postion of tuple 
print("POSTION OF INDIA : ",nation.index('INDIA'))
print("POSTION OF BHAVNAGAR : ",boxes.index('BHAVNAGAR'))

#COUNT SPECFIC VALUES OF TUPLE

print("COUNT OF INDIA IN TUPLE : ",nation.count('INDIA'))
print(" COUNT OF BHAVNAGAR IN TUPLE : ",boxes.count('BHAVNAGAR'))

#PRINT LIST TWICE 

print(boxes*2)

#CONCATE 2 TUPLE 
print(nation+boxes)
