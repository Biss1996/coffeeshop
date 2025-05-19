from app.order import Order

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        spender = None
        max_spent = 0
        for customer in set(order.customer for order in Order.all if order.coffee == coffee):
            total = sum(order.price for order in Order.all if order.customer == customer and order.coffee == coffee)
            if total > max_spent:
                spender = customer
                max_spent = total
        return spender
