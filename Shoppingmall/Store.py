class Store:
    def __init__(self):
        self.products = []

    def addProduct(self, product):
        # 기존 제품이 있는지 확인
        for _product in self.products:
            if _product.name == product.name:
                # 재고를 한 번에 증가시킴
                _product.stock += product.stock
                return  # 제품을 찾았으므로 메서드를 종료
        
        # 제품이 없을 경우 새로운 제품 추가
        self.products.append(product)

    def findProduct(self, product_name):
        # if product_name이 Store의 리스트에 있다면
        # 해당 product의 이름, 재고, 수량 출력
        for product in self.products:
            if (product.name == product_name):
                return f"Name: {product.name}, Price: {product.price}, Stock: {product.stock}"
        
        return "해당 제품을 찾을 수 없습니다."
    
    def listProducts(self):
        result = ""
        for product in self.products:
            if product.stock:
                result += self.findProduct(product.name) + "\n"

        return result