from Classes.ClassObjects.School_Class import Book


# Creating book instances
books = []
book1 = Book("1984", "George Orwell")
books.append(book1)
book2 = Book("To Kill a Mockingbird", "Harper Lee")
books.append(book2)

book3 = Book("save the Money","Gopi")
books.append(book3)

res = getattr(book3,"author")
print(res)

setattr(book3,"author","Gopi Kanna")
print(book3.author)

res1 = hasattr(book3,"author")
print(res1)
delattr()
"""

# Displaying details
book1.book_details()
book2.book_details()

# Borrowing a book
book1.borrow_book()
book1.book_details()

# Returning a book
book1.return_book()
book1.book_details()
"""

requiredbook = Book.available("1984")

for each in books:
    if requiredbook in each.tittle:
        print(each.book_details())
        if each.availability:
            each.borrow_book()