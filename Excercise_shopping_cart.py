item = input("enter the item you want to buy: ")
price = float(input("the price of item is: "))
quantity = int(input("enter the quantity of item: "))

total = quantity * price
print(f"you buy {quantity} {item} at the price of {price}")