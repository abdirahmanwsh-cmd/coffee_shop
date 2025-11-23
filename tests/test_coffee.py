import os
import sys
import pytest
from customer import Customer
from coffee import Coffee
from order import Order


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def setup_function():
    Order.all.clear()

def test_coffee_orders_customers_and_stats():
    c1 = Customer("C1")
    c2 = Customer("C2")
    coffee = Coffee("Americano")

    c1.create_order(coffee, 3.0)
    c2.create_order(coffee, 5.0)

    assert coffee.num_orders() == 2
    assert pytest.approx(coffee.average_price(), 0.01) == 4.0
    customers = coffee.customers()
    assert c1 in customers and c2 in customers
