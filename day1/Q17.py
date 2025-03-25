# 17. Bank Account Class
# 📌 Create a class BankAccount with attributes account_holder and balance. Add a
# method deposit() to add money and withdraw() to deduct money.

class BankAccount:
    def __init__(self, acc_holder, balance):
        self.acc_holder = acc_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print("deposit sucessful and your balance is ", self.balance)
    
    def withdraw(self, amount):
        self.balance -= amount
        print("withdraw was sucessul and your balance is ", self.balance)

acc_holder = print("enter name of account holder ")
balance = 67896478
account = BankAccount(acc_holder, balance)

ch = int(input(print("1. deposit money, 2. withdraw money ")))
if ch == 1:
    amount = int(input("enter amount "))
    account.deposit(amount)
elif ch ==2:
    amount = int(input("enter amount "))
    account.withdraw(amount)