# 14. Simple Calculator Using Functions
# 📌 *Write a calculator function that takes two numbers and an operator (+, -, , /) and returns the
# result.

def Calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif    operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2

num1 = int(input("enter 1st number "))
num2 = int(input("enter 2nd number "))
operator = input("enter the operator (+, -, *, /) ")

print(Calculator(num1, num2, operator))