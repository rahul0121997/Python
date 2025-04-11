from manager import Manager
class Fruit_Market():
    def __init__(self):
        self.mg = Manager()
        self.Fruit_menu()
    
    def Fruit_menu(self):
        print("WELCOME TO FRUIT MARKET")
        user_input = input(""""
                      1) Manager
                      2) Customer 
                      Select Your Role : """)
        if user_input == "1":
            self.mg.role_manager()

        elif user_input == "2":
            self.Customer()
                
        
f = Fruit_Market()