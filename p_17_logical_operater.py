#WAP FOR PERFORM ALL THE LOGICAL OPERATOR
#NAME : KRISHNADEEPSINH
#DATE:9/1/26

num1=int(input("ENTER NO1 :"))
num2=int(input("ENTER NO 2 : "))
num3=int(input("ENTER NO 3 : "))

result = num1<num2 and num2 <num3
print(f"{result} = {num1}<{num2} and {num2} <{num3}")

result = num1<num2 and num2 <num3
print(f"{result} = {num1}<{num2} and {num2} >{num3}")

result = num1<num2 or num2 <num3
print(f"{result} = {num1}<{num2} or {num2} <{num3}")

result = num1<num2 or num2 <num3
print(f"{result} = {num1}<{num2} or {num2} >{num3}")

result = not(num1<num2 or num2 <num3)
print(f"{result} = not {num1}<{num2} and {num2} <{num3}")
