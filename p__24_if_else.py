# write a program to find out which is cheaper product to purchase from 2 product's weight and price. 
# also display how much cheaper per gram 
#NAME:KRISHNADEEPSINH
#DATE:19/1/26

product1_price=float(input("ENTER THE PRICE OF PRODUCT 1 : "))
product1_wieght=float(input("ENTER THE WEIGHT OF PRODUCT 1 :"))

product2_price=float(input("ENTER THE PRICE OF PRODUCT 2 : "))
product2_wieght=float(input("ENTER THE WEIGHT OF PRODUCT 2 :"))

#calculate which product is cheaper per gram

product1_price_per_gram=product1_price/product1_wieght
product2_price_per_gram=product2_price/product2_wieght

if product1_price_per_gram<product2_price_per_gram:
    print("THE PRODUCT 1 IS CHEAPER : ",(product2_price_per_gram-product1_price_per_gram))
else:
    print("THE PRODUCT 2 IS CHEAPER : ",(product1_price_per_gram-product2_price_per_gram))
    