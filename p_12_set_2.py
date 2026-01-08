#WAP TO CREATE A SET AND PERFORM UNION , INTERSECTION & DIFFERENCE
# REMOVE DUPLICATE VALUES FORM THE LIST USING SET()
#NAME : KRISHNADEEPSINH
#DATE=08/1/26

set1={1,2,3,4,5}
set2={4,5,6,7,8}

print(set1,set2)

#union of set1 and set2
set3=set1.union(set2) 
print(set3)

#intersection of set1 and set2
set4=set1.intersection(set2)
print(set4)

#difference of set1 AND set2
set5=set1.difference(set2)
print(set5)


#list with duplicate value
numbers = [12, 45, 23, 12, 67, 89, 45, 34, 56, 78,23, 90, 11, 34, 67, 22, 56, 89, 90, 11]

print(len(numbers)) #length of the number list

#removing duplicate value from the list using set()
uni_no=set(numbers) # all the duplicate values are been removed
print(numbers)
 
