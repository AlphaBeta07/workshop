# 12. ATM Transaction System
# 📌 You are designing an ATM system where users can check their balance, withdraw money, or
# deposit money. Implement this using functions.

def ATM_sys():
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
ATM_sys()