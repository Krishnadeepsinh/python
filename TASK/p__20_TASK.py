#20. Given two lists, convert them into sets and find common elements.
#NAME : KRISHNADEEPSINH
#DATE : 12/1/26

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

list1=set(list1)
list2=set(list2)
print("COMMAN VALUE ARE :",list1.intersection(list2))