class Order:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculateTotal(self):
        return self.product.price * self.quantity
    
    def completeOrder(self):
        self.product.decreaseStock(self.quantity)