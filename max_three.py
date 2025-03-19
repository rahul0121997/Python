a = int(input("enter the number 1: "))
b = int(input("enter the number 2: "))
c = int(input("enter the number 3: "))

if a > b:
    if a > c:
        print("A is max")
    else:
        print("C is max")
elif b > c:
    print("B is max")

else:
    print("we can not print max between 0")