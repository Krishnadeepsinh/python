#14. Merge two dictionaries into a single dictionary.
#NAME=KRISHNADEEPSINH
#DATE=11/1/26

dic={'NAME':'KRISHNADEEPSINH',"AGE":19,'GENDER':'MALE','DOB':'2-MAY-2006','HOBBIES':'READING'}
stud={'KRISHNADEEPSINH':100,'YAGNADEEPSINH':90,'VIVEK R':70,'TUSHAR':80,'VIVEK S':81}
dic.update(stud)
print(dic)