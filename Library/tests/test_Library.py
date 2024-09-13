import unittest
from Library import Library
from Book import Book

class TestLibrary(unittest.TestCase):
    
    def setUp(self):
        self.library = Library()
        
        self.harry_porter = Book("Harry Porter", "Joan", "9788983927620", "Available")
        self.lord_of_ring = Book("Lord of Ring", "Tolkin", "9788950992460", "Available")
        self.the_mist = Book("The Mist", "King", "9781529379310", "Borrowed")
        
    def test_addBook(self):
        self.library.addBook(self.harry_porter)
        
        self.assertEqual(self.library.books, [self.harry_porter])
        
    def test_listAvailableBooks(self):
        self.library.addBook(self.harry_porter)
        self.assertEqual(self.library.listAvailableBooks(), "Harry Porter")
        
        self.library.addBook(self.lord_of_ring)
        self.assertEqual(self.library.listAvailableBooks(), "Harry Porter, Lord of Ring")
        
        self.library.addBook(self.the_mist)
        self.assertEqual(self.library.listAvailableBooks(), "Harry Porter, Lord of Ring")
        
    def test_borrowBook(self):
        self.library.addBook(self.harry_porter)
        self.library.borrowBook("9788983927620")
        self.assertEqual(self.harry_porter.status, "Borrowed")
        
    def test_returnBook(self):
        self.library.addBook(self.the_mist)
        self.library.returnBook("9781529379310")
        self.assertEqual(self.the_mist.status, "Available")