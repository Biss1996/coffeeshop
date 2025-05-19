import pytest
from app.customer import Customer
from app.coffee import Coffee

def test_customer_name_valid():
    c = Customer("Chris")
    assert c.name == "Chris"

def test_customer_name_invalid():
    with pytest.raises(ValueError):
        Customer("")

def test_create_order():
    c = Customer("Steve")
    coffee = Coffee("Black")
    order = c.create_order(coffee, 4.0)
    assert order.customer == c
    assert order.coffee == coffee
