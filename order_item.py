from order import Order
from product import Product

class OrderItem:
    def __init__(self, quantity, unitary_price, order, product):
        self._quantity = quantity
        self._unitary_price = unitary_price
        self._order = Order
        self._product = Product

        oi1 = OrderItem (149, 1.99, Order, Product)
        def mostrarpreco ():
            print(oi1._unitary_price)