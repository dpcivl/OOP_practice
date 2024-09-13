import unittest
from User import User
from Library import Library
from Book import Book

class TestUser(unittest.TestCase):
    def setUp(self):
        self.harry_porter = Book("Harry Porter", "Joan", "9788983927620", "Available")
        self.lord_of_ring = Book("Lord of Ring", "Tolkin", "9788950992460", "Borrowed")
        self.the_mist = Book("The Mist", "King", "9781529379310", "Borrowed")
        
        self.user_1 = User("Hyo in", [self.lord_of_ring, self.the_mist])
    
    def test_returnBook(self):
        self.user_1.returnBook(self.lord_of_ring)
        self.assertEqual(self.lord_of_ring.status, "Available")
        self.assertEqual(self.user_1.borrowed_books, [self.the_mist])
        
        
        
    def test_borrowBook(self):
        self.user_1.borrow(self.harry_porter)
        self.assertEqual(self.harry_porter.status, "Borrowed")
        # assertCountEqual = 순서 상관없이 리스트 비교
        self.assertCountEqual(self.user_1.borrowed_books, [self.lord_of_ring,
                                                      self.the_mist, self.harry_porter])