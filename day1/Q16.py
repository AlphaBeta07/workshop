# 16. Create a Student Class
# 📌 Create a class Student with attributes name and marks. Add a method to check if the
# student has passed (pass mark: 40).

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def PNP(self):
        return self.marks >= 40
    
name = input("enter name ")
marks = int(input("enter marks "))

student = Student(name, marks)

if student.PNP():
    print("Passed")
else:
    print("not passed")