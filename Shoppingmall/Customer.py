class Customer:
    def __init__(self, name, orders):
        self.name = name
        self.cart = orders

    def addToCart(self, product):
        self.cart.append(product)

    def checkout(self):
        total = 0

        # order_list에 있는 Order 전부 완료 처리
        for order in self.cart:
            order.completeOrder()
            total += order.calculateTotal()

        print(f"총 금액은 {total}원입니다.\n")

        self.cart.clear()