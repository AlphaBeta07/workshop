# 1. Identify the Employee Category
# A company categorizes its employees based on their salaries:
# Salary above ₹50,000 → "High Income"
# Salary between ₹30,000 and ₹50,000 → "Medium Income"
# Salary below ₹30,000 → "Low Income"
# Write a Python program that takes an employee’s salary as input and prints their category.

salary = int(input("enter salary : "))

if salary > 50000:
    print("high income")
elif salary < 50000 and salary >30000 :
    print("medium income")
elif salary < 30000:
    print("low income")