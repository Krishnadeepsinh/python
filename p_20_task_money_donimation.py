'''write a program to display dinominations of currency for given amount
input : 887 Rupees 
output : 
500 x 1 = 500
200 x 1 = 200
100 x 1 = 100
50 x 1 =  50
20 x 1 =  20
10 x 1 =  10
5 x 1 =   05
2 x 1 =   02
1 x 1 =   01'''

amount=int(input("ENTER AMOUNT OF MONEY : "))

rs500=amount//500;
amount=amount%500
print("500rs note required :",rs500)

rs200=amount//200;
amount=amount%200
print("200rs note required :",rs200)

rs100=amount//100;
amount=amount%100
print("100rs note required :",rs100)

rs50=amount//50;
amount=amount%50
print("50rs note required :",rs50)

rs20=amount//20;
amount=amount%20
print("20rs note required :",rs20)

rs10=amount//10;
amount=amount%10
print("10rs note required :",rs10)

rs5=amount//5;
amount=amount%5
print("5rs coin required :",rs5)

rs2=amount//2;
amount=amount%2
print("2rs coin required :",rs2)

rs1=amount//1;
amount=amount%1
print("1rs coin required :",rs1)
