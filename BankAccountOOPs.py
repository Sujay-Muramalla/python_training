#BankAccountOOPs.py

# Define Bank Account Below:

class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0
    
    def getBalance(self):
        return self.balance
        
    def deposit(self,amount_deposit):
        self.balance=self.balance+amount_deposit
        return self.balance
    
    def withdraw(self, amount_withdraw):
        self.balance = self.balance - amount_withdraw
        return self.balance
        
acct = BankAccount("Darcy")
print (acct.owner) #Darcy
print (acct.balance) #0.0
print (acct.deposit(10))  #10.0
print (acct.withdraw(3))  #7.0
print (acct.getBalance()) #7.0
print (acct.balance)


class BankAccount:
 
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0
 
    def getBalance(self):
        return self.balance
 
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
 
    def deposit(self, amount):
        self.balance += amount
        return self.balance


