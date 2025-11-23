# Simple interactive debug script. Run this file to try the domain model.


if __name__ == "__main__":
 from customer import Customer
from coffee import Coffee
from order import Order


# reset any previous orders (useful if you import multiple times)
Order.all.clear()


# create customers
alice = Customer("Alice")
bob = Customer("Bob")


# create coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")


# create orders
alice.create_order(latte, 4.5)
alice.create_order(espresso, 3.0)
bob.create_order(latte, 7.0)
bob.create_order(latte, 6.0)


print("All orders:", Order.all)
print("Latte num orders:", latte.num_orders())
print("Latte avg price:", latte.average_price())
print("Customers who ordered Latte:", latte.customers())
print("Alice's coffees:", alice.coffees())
print("Most aficionado for Latte:", Customer.most_aficionado(latte))

