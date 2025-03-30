# ATM using oops with Comments

class ATM:
    def __init__(self):
        self.pin = ""                  # Initialize PIN as empty string
        self.balance = 0               # Initialize balance to zero
        # self.menu()                    # Call the menu method when object is created
        
    def menu(self):
        user_input = input("""
                        select operation!
                        1. Set pin
                        2. Deposit
                        3. Withdraw
                        4. Check balance
                        5. Exit
                        """)           # Display menu options and get user input
        
        if user_input == "1":          # If user selected option 1
           self.creat_pin()            # Call the create_pin method
        elif user_input == "2":        # If user selected option 2
            self.deposit()             # Call the deposit method
        elif user_input == "3":        # If user selected option 3
            self.withdraw()            # Call the withdraw method
        elif user_input == "4":        # If user selected option 4
            self.check_balance()       # Call the check_balance method
        elif user_input == "5":        # If user selected option 5
            print("exit")              # Print exit message
        else:
            print("invalid operation") # Print error message for invalid input

    def creat_pin(self):
            self.pin = input("enter your pin: ")  # Get new PIN from user
            print("you successfully set your pin") # Confirm PIN was set
            self.menu()                # Return to main menu
            
    def deposit(self):
        tem = input("enter your pin: ")  # Ask user for PIN
        if tem == self.pin:             # Verify PIN is correct
            amount = int(input("enter the amount you want to deposit: "))  # Get deposit amount
            self.balance = self.balance + amount  # Add deposit to balance
            print("deposit successfully")  # Confirm deposit was successful
            self.menu()                # Return to main menu
            
    def withdraw(self):
        temp = input("enter the pin: ")  # Ask user for PIN
        if temp == self.pin:            # Verify PIN is correct
            amount = int(input("enter the amount you want to : "))  # Get withdrawal amount
            if amount <= self.balance:  # Check if sufficient balance
                self.balance = self.balance - amount  # Subtract withdrawal from balance
                print("you successfully withdraw amount")  # Confirm withdrawal
            else:
                print("insuffucient balance")  # Inform user of insufficient funds
        self.menu()                    # Return to main menu
        
    def check_balance(self):
        temp = input("enter the pin: ")  # Ask user for PIN
        if temp == self.pin:            # Verify PIN is correct
            print(self.balance)         # Display current balance
        self.menu()                    # Return to main menu

sbi = ATM()                       # Create an instance of the ATM class 

sbi.menu() # self.menu() inside constructor do the same but difference is it is called autometically sbi.menu() we have call it