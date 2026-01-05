#WAP TO CREATE LIST & PERFORM VARIOUS 
#FUNCTIONS(APPEND,COUNT,COPY,REMOVE,DEL,POP,CLEAR,)
#NAME=KRISHNADEEPSINH
#DATE=5/1/2026

list=['apple','krish','bottle','compass','apple',100,3.14,'apple',True,None,False]

list2=list.copy()                                   #copy(copy a list to another )
list.insert(0,'banana')                             #insert specfic
print(list)
list[1]='kiwi'                                      #update list
print(list)                                         
print(list.append('KD'))                             #append(add new data at end )
print(list)                         
print(list.count('apple'))                          #count(count specfic value in list)
print(list.remove(True))                            #remove(remove specfic value in list )
del list[0]                                         #delete(delete value from list on index)
print(list.pop(False))                              #pop(delete value from list on index)
print(list)                             
list.clear()                                        #clear(empty/remove all value from list)

print(list)
print(list2)