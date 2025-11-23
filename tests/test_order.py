import os
import sys
import pytest


from customer import Customer
from coffee import Coffee
from order import Order

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))




def setup_function():
    Order.all.clear()

def test_order_creation_and_validation():
    c = Customer("Ann")
    k = Coffee("Mocha")

    o = Order(c, k, 5.0)
    assert o in Order.all
    assert o.customer is c
    assert o.coffee is k
    assert o.price == 5.0

    with pytest.raises(TypeError):
        Order("not a customer", k, 5.0)
    with pytest.raises(TypeError):
        Order(c, "not a coffee", 5.0)
    with pytest.raises(ValueError):
        Order(c, k, 0.5)
