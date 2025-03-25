# 7. ATM Cash Dispensing Machine
# An ATM machine dispenses only ₹500 and ₹2000 notes. Write a Python program that takes an
# amount as input and prints how many ₹2000 and ₹500 notes will be given, assuming the
# amount is a multiple of 500.

amount = int(input("enter amount "))
if amount % 500 != 0:
    print("invald amount")

note_2000 = amount // 2000
remaining = amount % 2000
note_500 = remaining // 500

print("total ₹2000 notes are ", note_2000)
print("total ₹500 notes are ", note_500)