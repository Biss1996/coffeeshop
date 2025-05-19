from app.customer import Customer
from app.coffee import Coffee
from app.order import Order

c1 = Customer("Alice")
c2 = Customer("Bob")
c3 = Customer("Eve")

coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

c1.create_order(coffee1, 4.5)
c1.create_order(coffee2, 3.0)
c2.create_order(coffee1, 5.0)
c3.create_order(coffee1, 6.5)

print("Most aficionado for Latte:", Customer.most_aficionado(coffee1).name)
