class Account:
    def __init__(self, balance = 0):
        self.__balance = balance
    
    def getBalance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance = self.__balance + amount         
        print(f"success, actual balance is: {acc.getBalance()}")
        self.__log_transaction()
        return self.__balance
    
    def __log_transaction(self):
        print("Internal registration: operation completed.")
    
acc = Account(90)

acc.deposit(90)

print(acc.getBalance())
