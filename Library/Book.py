class Book:
    def __init__(self, title, author, isbn, status):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status
        
    def borrow(self):
        if self.status == "Available": self.status = "Borrowed"
        else: raise ValueError("The Book is NOT AVAILABLE")
    
    def returnBook(self):
        if self.status == "Borrowed": self.status = "Available"
        else: raise ValueError("CAN'T return if you didn't borrow")