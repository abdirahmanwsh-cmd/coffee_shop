import os
import sys
import pytest
from customer import Customer
from coffee import Coffee
from order import Order

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def setup_function():
    Order.all.clear()

def test_customer_orders_and_coffees():
    c = Customer("Tom")
    co = Coffee("Flat White")

    c.create_order(co, 4.0)
    c.create_order(co, 5.0)

    assert len(c.orders()) == 2
    assert co in c.coffees()

def test_most_aficionado():
    a = Customer("A")
    b = Customer("B")
    co = Coffee("Cappuccino")

    a.create_order(co, 2.0)
    a.create_order(co, 3.0)
    b.create_order(co, 6.5)

    assert Customer.most_aficionado(co) is b

    co2 = Coffee("Matcha")
    assert Customer.most_aficionado(co2) is None
