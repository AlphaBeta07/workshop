# 19. Create a Rectangle Class
# 📌 Create a class Rectangle with attributes length and width. Add a method area() and
# perimeter() to calculate the area and perimeter.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def Area(self, length, width):
        print("area is ", length * width)
    
    def perimeter(self, length, width):
        print("perimeter is", 2 * length + 2 * width)

length = int(input("enter length "))
width = int(input("enter width "))

rectangle = Rectangle(length, width)

rectangle.Area(length, width)
rectangle.perimeter(length, width)