import pytest
from app.coffee import Coffee
from app.customer import Customer
from app.order import Order

def setup_function():
    Order.all.clear()

def test_coffee_name_valid():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"

def test_coffee_name_invalid():
    with pytest.raises(ValueError):
        Coffee("Hi")  

def test_orders_and_customers_for_coffee():
    c1 = Customer("John")
    c2 = Customer("Wick")
    coffee = Coffee("White")
    Order(c1, coffee, 2.5)
    Order(c2, coffee, 3.0)

    assert len(coffee.orders()) == 2
    customers = coffee.customers()
    assert c1 in customers
    assert c2 in customers
    assert len(customers) == 2

def test_num_orders_and_average_price():
    coffee = Coffee("Americano")
    c1 = Customer("Mark")
    c2 = Customer("Daniel")
    Order(c1, coffee, 4.0)
    Order(c2, coffee, 6.0)

    assert coffee.num_orders() == 2
    assert coffee.average_price() == 5.0
