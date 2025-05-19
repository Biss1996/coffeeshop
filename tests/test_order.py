import pytest
from app.customer import Customer
from app.coffee import Coffee
from app.order import Order

def setup_function():
    Order.all.clear()

def test_order_creation_and_attributes():
    c = Customer("Tom")
    coffee = Coffee("Latte")
    order = Order(c, coffee, 3.5)

    assert order.customer == c
    assert order.coffee == coffee
    assert order.price == 3.5
    assert order in Order.all

def test_invalid_customer_type():
    coffee = Coffee("Latte")
    with pytest.raises(TypeError):
        Order("NotACustomer", coffee, 3.0)

def test_invalid_coffee_type():
    customer = Customer("Jane")
    with pytest.raises(TypeError):
        Order(customer, "NotACoffee", 3.0)

def test_invalid_price_type_and_range():
    c = Customer("Joe")
    coffee = Coffee("Espresso")

    with pytest.raises(ValueError):
        Order(c, coffee, 0.5)  #  low price

    with pytest.raises(ValueError):
        Order(c, coffee, 11.0)  # high price

    with pytest.raises(ValueError):
        Order(c, coffee, "not-a-float")  # Not a float
