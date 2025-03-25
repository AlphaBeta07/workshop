# 5. ATM PIN Verification
# A bank ATM allows a user to enter their PIN a maximum of 3 times. If the correct PIN (1234) is
# entered within 3 attempts, the user gains access; otherwise, the card is blocked. Write a Python
# program for this.

pin = int(input("enter pin "))
i = 1
while i < 3:
    if pin == 1234:
        print("You have gained access")
        break
    else:
        i += 1        
        pin = int(input("enter pin "))
else:
    print("the card has been bocked")
 