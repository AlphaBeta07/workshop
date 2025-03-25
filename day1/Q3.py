# 3. Imagine you are designing a basic ATM-like interface where users can:
# 1. Check Balance
# 2. Deposit Money
# 3. Withdraw Money
# 4. Exit the System
# Your Task: Write a Python program that displays a menu, takes user input, and performs the
# respective operation based on the user's choice.


balance = 12576
while True:
    print("1. Check Balance  2. Deposit Money 3. Withdraw Money 4. Exit the System")
    ch = int(input("Enter Choice "))
    if ch == 1:
            print("your balance is ", balance)
    elif ch == 2:
            deposit = int(input("enter the amount of cash deposit "))
            balance += deposit
    elif ch == 3:
            withdraw = int(input("enter the amount of withdraw "))
            balance -= withdraw
    elif ch == 4:
            break

        