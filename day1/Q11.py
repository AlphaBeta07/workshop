# 11. Removing Duplicates from a List - Set
# 📌 A librarian is digitizing book records but some book titles are repeated. Write a program to
# remove duplicates from a list using a set.

book = input("enter book name (add comma between name of book)" ).split(",")

list_book = list(set(book))
print("name of books are ")
for book in list_book:
    print(book)