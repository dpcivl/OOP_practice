class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def decreaseStock(self, quantity=1):
        if (self.stock <= 0):
            raise ValueError("재고가 없습니다.")
        self.stock -= quantity

    def increaseStock(self, quantity=1):
        self.stock += quantity