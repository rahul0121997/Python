class Manager:
    def __init__(self):
        pass
    
    def role_manager(self):
        print("Fruit Market Manager")
        user_input = input("""
                           1) Add Fruit Stock
                           2) View Fruit Stock
                           3) Update Fruit Stock
                           Enter Your Choice: 
                           """)
        if user_input == "1":
            file = open("fruit.txt", "w")
            print("ADD FRUIT STOCK")
            self.fruit_name = input("Enter Fruit Name: ")
            self.fruit_kg = input("Enter Fruit Qty(in kg): ")
            self.fruit_price = input("Enter Fruit Price: ")
            file.write(f"{self.fruit_name}: Quantity = {self.fruit_kg} kg, Price = {self.fruit_price}\n")
            file.close()
        elif user_input == "2":
            print("VIEW FRUIT STOCK")
            file = open("fruit.txt", "r")
            view_fruit = file.read()
            print(view_fruit)
            file.close()
            
        elif user_input == "3":
            print("UPDATE FRUIT STOCK")
            self.fruit_name = input("Enter Fruit Name: ")   
            file = open("fruit.txt", "r")   
            fruit_data = file.readlines()   
            file.close()
            updated_data = []
            for line in fruit_data:
                if self.fruit_name in line:
                    self.fruit_kg = input("Enter New Quantity: ")
                    self.fruit_price = input("Enter New Price: ")
                    updated_data.append(f"{self.fruit_name}: Quantity = {self.fruit_kg} kg, Price = {self.fruit_price}\n")
                else:
                    updated_data.append(line)
                file = open("fruit.txt", "w")
                file.writelines(updated_data)
                file.close()
                print("Fruit Stock Updated Successfully")
                
