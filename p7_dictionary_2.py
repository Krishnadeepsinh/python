#WAP PROGRAM CREATE EMPTY DICTIONARY & ADD KEYPAIR VALUE 
# AND ALSO ADD NESTED TUPLE INSIDE DICTIONARY & ALSO LIST IN IT PRINT  
#NAME=KRISHNADEEPSINH
#DATE=6/1/2026

book = {}
print(book)
book['name']='atomic habits'
book['author']='james clear'
book['price']='350'
print(book)

book['tuple_chapter']=(1,2,3,4,5)
book['list_subject']=['history','biology','maths']

print(book)
print(book['tuple_chapter'][1])
print(book['list_subject'][1])


