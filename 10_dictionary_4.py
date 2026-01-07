#WAP PROGRAM CREATE DICTIONARY AND PERFORM VARIOUS OPERATION/FUNCTION
#LIKE COPY,UPDATE,PRINT KEY,VALUE ITEMS,FROMKEYS,POP,POPITEMS
#NAME:KD
#DATE=7/1/26

person = {'name':'rahul sharma','age':40,'weight':74.22,'gender':True,'isMarried':False}

print(person)
print(person.get('name'))
#print(person['city'])      #error
#print(person.get('city'))  # error would not ocuur happen if city

person2=person.copy()       #create a shallow copy of person into person2
print(person)
print(person2)
person2.clear()              #person2 dictionary would be clear

print(person.keys())
print(person.values())
print(person.items())

detail_list=["name","age","gender"]
bio=dict.fromkeys(detail_list)
print(bio)
bio['name']='kd'
bio['age']=19
bio['gender']='male'
print(bio)
bio.pop('gender')
bio.pop('city',False)