#WAP TO PURCHASE A PROGRAM AND THEN SELL AND FIND OUT EITHER PROFIT OR LOSS IN IT
#NAME : KRISHNADEEPSINH
#DATE : 15/1/2026

PURCHASE_PRICE=float(input("ENTER THE PURCHASE PRICE : "))
SELLING_PRICE=float(input("ENTER THE SELLING PRICE : "))
difference=SELLING_PRICE-PURCHASE_PRICE

if difference>0:
    print("PROFIT IS = ",difference)
if difference<0:
    print("LOSS IS = ",difference)
if difference==0:
    print("NO LOSS NO PROFIT")
