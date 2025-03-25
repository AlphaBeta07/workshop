# 8. Shopping Cart - List Operations
# 📌 You are creating a shopping cart program. Users should be able to add items to the cart and
# view the final list. Implement a program that allows a user to add items (names of products) until
# they type "done" and then prints all the items in the cart

cart = []
while True:
    item = input("Enter item (type done after add all items): ").strip()
    if item.lower() == "done":
        break
    cart.append(item)
    
print("Items are ")
for product in enumerate(cart, start=1):
    print(product)