class BankAccount:
    
    def __init__(self,username, balance=0.0):
        self.username = username
        self.balance = balance
        
    def welcome(self):
        print (f"welcome {self.username}, congratulations for opening the bank account with us!")
        
        
    def deposit(self,amount):
        self.balance = self.balance + amount
        print (f"Dear {self.username}, you deposited {amount} on your account, and your current balance is: {self.balance}")
        

u1 = BankAccount("Sujay")
u1.welcome()

inp=''
while (inp!='n'):
    inp = input("would you like to deposit in your account? ")
    if (inp=='y'):
        amt = float (input("enter the amount you would like to deposit: "))
        u1.deposit(amt)
    



