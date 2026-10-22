books = {}


def add_book(book_id, title, author):
    books[book_id] = {
        "title": title,
        "author": author,
        "available": True
    }
    print("Book added successfully")


def search_book(book_id):
    if book_id in books:
        print("Book Details:", books[book_id])
    else:
        print("Book not found")


def issue_book(book_id):
    if book_id in books and books[book_id]["available"]:
        books[book_id]["available"] = False
        print("Book issued successfully")
    else:
        print("Book not available")


def return_book(book_id):
    if book_id in books and not books[book_id]["available"]:
        books[book_id]["available"] = True
        print("Book returned successfully")
    else:
        print("Book cannot be returned")


def display_books():
    print("Available Books:")
    for book_id, details in books.items():
        if details["available"]:
            print(book_id, details["title"], details["author"])


add_book(101, "Python Basics", "John")
add_book(102, "Learn Java", "Smith")

search_book(101)
issue_book(101)
return_book(101)
display_books()