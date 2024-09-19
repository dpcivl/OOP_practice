import unittest
from Order import Order
from Product import Product

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.test_product = Product("Ramen", 15000, 5)
        self.order = Order(self.test_product, 2)

    def test_calculateTotal(self):
        total = self.order.calculateTotal()

        self.assertEqual(total, 30000)

    def test_completeOrder(self):
        self.order.completeOrder()

        self.assertEqual(self.test_product.stock, 3)