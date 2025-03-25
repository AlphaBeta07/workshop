# 23. E-Commerce Product Management
# 📌 Create a class Product with attributes name, price, and stock. Add a method
# purchase() that reduces stock if available.

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price 
        self.stock = stock
    
    def Purchase(self, quantity):
        quantity = self.stock
        