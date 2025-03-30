opertor = input("enter the operation you want to perform (+,-,*,/,%)")
num1 = float(input("enter number number 1: "))
num2 = float(input("enter number number 2: "))

if opertor == "+":
    result = num1 + num2
    print(round(result,3))

elif opertor == "-":
    result = num1 - num2
    print(result,3)

elif opertor == "*":
    result = num1 * num2
    print(result,3)

elif opertor == "/":
    result = num1 / num2
    print(result,3)

elif opertor == "%":
    result = num1 % num2
    print(round(result,3))

else:
    print("invalid opertion")




