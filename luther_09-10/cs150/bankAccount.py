class BankAccount:
    def __init__(self,ownerID):
        self.id = ownerID
        self.balance = 0

    def getBalance(self):
        return self.balance

    def getOwner(self):
        return self.id

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance = self.balance - amount
        else:
            print("Not enough money in account to complete transaction")
                    

    def transfer(self, accountTwo, amount):
        self.withdraw(amount)
        accountTwo.deposit(amount)
    
        
        
