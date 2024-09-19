import unittest

from Product import Product
from Store import Store

class TestStore(unittest.TestCase):
    def setUp(self):
        self.store = Store()
        self.snack = Product("snack", 1000, 2)
        self.cookie = Product("cookie", 500, 10)

    def test_addProduct(self):
        self.store.addProduct(self.snack)
        self.assertEqual(self.store.products, [self.snack])

    def test_findProduct(self):
        self.store.addProduct(self.snack)
        result = self.store.findProduct("snack")

        self.assertEqual(result, "Name: snack, Price: 1000, Stock: 2")

    def test_findProduct_WhenNotInList(self):
        result = self.store.findProduct("snack")

        self.assertEqual(result, "해당 제품을 찾을 수 없습니다.")

    def test_listProducts(self):
        self.store.addProduct(self.snack)
        self.store.addProduct(self.cookie)

        # products에 있는 product의 정보 전부 꺼내기
        result = self.store.listProducts()

        self.assertEqual("Name: snack, Price: 1000, Stock: 2\nName: cookie, Price: 500, Stock: 10\n", result)

