from collections import Counter
x = int(input("enter the number of shoes: "))

shoes_size = list(map(int,input("enter the size of the shoe: ").split()))

number_of_customers = int(input("enter the number of customer: "))

stock = Counter(shoes_size)
print(stock)

total_price = 0

for i in range(number_of_customers):
    size,price = map(int , input("enter the size and price: ").split())
    
    if stock[size] > 0:
        total_price += price
        stock[size] -= 1
    
print(total_price)


