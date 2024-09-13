from Library import Library
from Book import Book
from User import User

harry_porter = Book("Harry Porter", "Joan", "9788983927620", "Available")
lord_of_ring = Book("Lord of Ring", "Tolkin", "9788950992460", "Borrowed")
the_mist = Book("The Mist", "King", "9781529379310", "Borrowed")
        
library = Library()

library.addBook(harry_porter)
library.addBook(lord_of_ring)
library.addBook(the_mist)

hyoin = User("Hyoin", [lord_of_ring, the_mist])
print(library.listAvailableBooks())    # "Harry Porter"

hyoin.returnBook(lord_of_ring)
print(library.listAvailableBooks())    # "Harry Porter, Lord of Ring"

hyoin.returnBook(the_mist)
print(library.listAvailableBooks())    # "Harry Porter, Lord of Ring, The Mist"

hyoin.borrow(harry_porter)
print(library.listAvailableBooks())    # "Lord of Ring, The Mist"

library.borrowBook("9788950992460")
print(library.listAvailableBooks())