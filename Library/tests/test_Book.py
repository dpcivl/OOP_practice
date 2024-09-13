import unittest
from Book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.harry_porter = Book("Harry Porter", "Joan", "9788983927620", "Available")
        self.lord_of_ring = Book("Lord of Ring", "Tolkin", "9788950992460 ", "Available")
        self.the_mist = Book("The Mist", "King", "9781529379310 ", "Borrowed")
        
    def test_borrow(self):
        self.harry_porter.borrow()
        
        self.assertEqual(self.harry_porter.status, "Borrowed")
        
    def test_borrow_whenNotAvailable(self):
        with self.assertRaises(ValueError):
            self.the_mist.borrow()
        
    def test_returnBook(self):
        self.the_mist.returnBook()
        
        self.assertEqual(self.the_mist.status, "Available")
        
    def test_returnBook_whenNotBorrowed(self):
        with self.assertRaises(ValueError):
            self.lord_of_ring.returnBook()