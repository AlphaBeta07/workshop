# 2 . Odd or Even Streetlight System
# A city uses an even-odd rule to manage electricity usage in streetlights. Streetlights with even
# numbers are turned on at night, while odd-numbered lights remain off. Write a program that
# takes a streetlight number as input and prints whether it should be ON or OFF

num = int(input("enter stree light number "))

if num % 2 == 0:
    print("ON")
else:
    print("OFF")