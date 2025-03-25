# 18. Create a Book Class
# 📌 Create a class Book with attributes title and author. Add a method to display book
# details.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def details(self):
        print("Book title is ",title)
        print("Author is ",author)

title = input("enter title of book ")
author = input("enter the author ")

book = Book(title,author)
print("the book details are ")
book.details()