# encapsulation

class Atm:
    def __init__(self, balance):
        self.__balance = balance
        self.__pin = 1234
        
    def get_balance(self):
        return self.__balance
    
    def set_balance(self,amount):
        if amount > 0:
            self.__balance = amount 

a = Atm(1000)
a.set_balance(2000)
print(a.get_balance())
