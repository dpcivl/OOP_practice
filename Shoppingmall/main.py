from Store import Store
from Customer import Customer
from Order import Order
from Product import Product

store = Store()

cookie = Product("cookie", 500, 10)
snack = Product("snack", 1000, 2)

store.addProduct(cookie)
store.addProduct(snack)

print(store.listProducts())

cookie_2 = Product("cookie", 500, 2)

store.addProduct(cookie_2)

print(store.listProducts())

order_cookie = Order(cookie, 7)
order_snack = Order(snack, 1)
orders = []

customer = Customer("Peter", orders)
customer.addToCart(order_cookie)
customer.addToCart(order_snack)

customer.checkout()

print(store.listProducts())