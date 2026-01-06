#WAP TO CREATE A DICTIONARY & INSERT UPDATE & DELETE DICTIONARY
#NAME=KRISHNADEEPSINH
#DATE=6/1/2026

person={'name':'krishnadeepsinh','age':19,'weight':82,'gender':'male'}

print(person)                           
print(person['name'])               #print specific
person['weight']=85                 #update dictionary data

person['city']='bhavnagar'          #insert data in dictionary

del person['gender']                #delete data from dictionary
print(person)
