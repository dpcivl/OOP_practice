import unittest
from Product import Product

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product("Coke", 17000, 5)

    def test_decreaseStock(self):
        self.product.decreaseStock()

        self.assertEqual(self.product.stock, 4)

    def test_decreaseStockWhenNotAvailable(self):
        for i in range(5):
            self.product.decreaseStock()

        with self.assertRaises(ValueError):
            self.product.decreaseStock()

    def test_increaseStock(self):
        self.product.increaseStock()

        self.assertEqual(self.product.stock, 6)