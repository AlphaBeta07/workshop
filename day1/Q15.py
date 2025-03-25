# 15. Find the Maximum of Three Numbers
# 📌 Write a function that takes three numbers as input and returns the maximum of the three

def Number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3

num1 = int(input("enter 1st number "))
num2 = int(input("enter 2nd number "))
num3 = int(input("enter 3rd number "))
print("largest number is ",Number(num1, num2, num3))