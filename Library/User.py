class User:
    def __init__(self, name, books):
        self.name = name
        self.borrowed_books = books
        
    def returnBook(self, book):
        if (book.status == "Borrowed"):
            book.returnBook()
            self.borrowed_books.remove(book)
        
    def borrow(self, book):
        if (book.status == "Available"):
            book.borrow()
            self.borrowed_books.append(book)