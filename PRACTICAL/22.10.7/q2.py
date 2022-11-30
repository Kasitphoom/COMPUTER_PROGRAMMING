class BankAccount:
    def __init__(self, name, ownername, accountno, balance):
        self.name = name
        self.ownername = ownername
        self.accountno = accountno
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Unable to widthdraw from account {self.accountno}: Insufficient funds")
            return
        self.balance -= amount
        
    def printbal(self):
        print(f"Balance (account {self.accountno}): {self.balance}")
        
b = BankAccount("Kbank", "John", 123456789, 1000)

b.printbal()
b.deposit(100)
b.printbal()
b.withdraw(3000)
b.printbal()