# 25. Employee Salary Increment System 
# Create a class Employee with attributes name and salary. Add a method apply_raise() 
# that increases the salary by a given percentage.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def apply_raise(self, Salary):
        self.salary = Salary + (percent / 100 ) * Salary
        print("the salary will be ", self.salary)

name = input("enter name ")
Salary = int(input("enter salary "))
percent = int(input("enter percentage "))

percentage = Employee(name, Salary)
percentage.apply_raise(Salary)