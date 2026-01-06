"""create tuple to store all states name of india 
display tuple 
display 1st five items 
display 2nd and 3rd and 4th item 
display all items from 7th position onwards 
try to remove 3rd item see what happens """

states= ("Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal")

print(states)               #print all states
print(states[0:5])          #print first 5 data
print(states[2:5])          #print 2nd ,3rd,4th data
print(states[6:])           #print data from 7th to end
# del states[3]             #error occuer on deleting of data not supported in tuple bcz immutable