from Book import Book

class Library:
    def __init__(self, name="IlGwang"):
        self.books = []
        self.name = name
        
    def addBook(self, book):
        # book은 책 인스턴스여야 함.
        self.books.append(book)
        
    def listAvailableBooks(self):
        book_list = []
        result = ""
        
        if not self.books:
            return "No book in here"
        
        for book in self.books:
            if (book.status == "Available"):
                book_list.append(book.title)
                
        for book in book_list:
            if (book == book_list[len(book_list)-1]):
                result += book
            else:
                result += book + ", "
                
        return result
    
    def borrowBook(self, ISBN):
        for book in self.books:
            if (ISBN == book.isbn):
                book.borrow()
                return
        raise ValueError("Invalid ISBN")
            
    def returnBook(self, ISBN):
        for book in self.books:
            if (ISBN == book.isbn):
                book.returnBook()
                return
        raise ValueError("Invalid ISBN")