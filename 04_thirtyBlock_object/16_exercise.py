class Account:
    def __init__(self, balance = 0):
        self.__balance = balance
    
    def getBalance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance = self.__balance + amount         
        print(f"success, actual balance is: {acc.getBalance()}")
        return self.__balance
    
acc = Account(90)

acc.deposit(90)

print(acc.getBalance())
print(f"The balance is: {acc.__balance}") #fallisce

