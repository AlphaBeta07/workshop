# 6. Reverse a Number
# Write a Python program to reverse a given number. For example, if the input is 12345, the
# output should be 54321.

num = int(input("enter number "))
rev_num = int(str(num)[::-1])
print("the reversed number is ", rev_num)