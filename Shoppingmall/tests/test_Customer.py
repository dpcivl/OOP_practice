import unittest
from Customer import Customer
from Product import Product
from Order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.ramen = Product("ramen", 2000, 8)
        self.cookie = Product("cookie", 500, 10)
        self.snack = Product("snack", 1000, 2)
        self.order_ramen = Order(self.ramen, 3)
        self.order_cookie = Order(self.cookie, 2)
        self.order_snack = Order(self.snack, 2)
        self.orders = []
        self.customer = Customer("Peter", self.orders)

    def test_addToCart(self):
        self.customer.addToCart(self.order_ramen)
        self.customer.addToCart(self.order_cookie)
        self.customer.addToCart(self.order_snack)

        # 주문 리스트 확인
        self.assertEqual(self.customer.cart, [self.order_ramen, self.order_cookie, self.order_snack])

    def test_checkout(self):
        self.customer.addToCart(self.order_ramen)
        self.customer.addToCart(self.order_cookie)
        self.customer.addToCart(self.order_snack)

        self.customer.checkout()

        # 각 주문 건들에 대하여 product 재고가 감소했는지 확인
        self.assertEqual(self.ramen.stock, 5)
        self.assertEqual(self.cookie.stock, 8)
        self.assertEqual(self.snack.stock, 0)

        # 재고가 없음에도 구매 확정
        with self.assertRaises(ValueError):
            self.customer.addToCart(self.order_snack)
            self.customer.checkout()
