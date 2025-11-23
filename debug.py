


if __name__ == "__main__":
 from customer import Customer
from coffee import Coffee
from order import Order


Order.all.clear()

alice = Customer("Alice")
bob = Customer("Bob")



latte = Coffee("Latte")
espresso = Coffee("Espresso")



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

