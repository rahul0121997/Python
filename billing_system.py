def food():
    print("welcome to the food menu")
    print("*****--------------*****")
    print()
    print(
        "1. pizza       RS 230"
        "\n2. burger      RS 120"
        "\n3. idli        RS 100"
        "\n4. dosa        RS 80"
        "\n5. exit"
    )

    price = 0
    total = 0
    while True:
        choice = int(input("enter your choice(1-5) :"))
        if choice < 1 or choice > 5:
            print("enter the valid choice(1-5)")
            continue

        if choice == 5:
            break
        quantity = int(input("enter the quantity: "))
        if quantity < 1:
            print("quantity must be positive")
            continue
        if choice == 1:
            print("you chose pizza")
            price = 230 *quantity
        elif choice == 2:
            print("you chose burger")
            price = 120 * quantity
        elif choice == 3:
            print("you chose idli")
            price = 100 * quantity
        elif choice == 4:
            print("you chose dosa")
            price = 80 * quantity
        print(f"the price is:{price}")
        total = total + price


    print(f"the total bill is : {total}")
    print("thanks for visiting!!!")
    
food()
