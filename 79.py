class BankAccount():
    def __init__(self, balance):
        self.__balance = balance
        
    @property
    def balance(self):
        print("getting balance")
        return self.__balance
    
     
    @balance.setter
    def balance(self,amount):
        if amount > 0:
            self.__balance = amount
        else:
            print("Balance can not be negative")
            
    @balance.delete
    def balance(self):
        del self.__balance
        

acc = BankAccount(1000)
print(acc.balance)
acc.balance = 500
# del acc.balance
print(acc.balance)
