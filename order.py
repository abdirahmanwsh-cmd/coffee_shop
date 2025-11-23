class Order:
    """Order class connecting Customer and Coffee.

    - customer: Customer instance
    - coffee: Coffee instance
    - price: float between 1.0 and 10.0

    All orders are kept in Order.all
    """

    all = []

    def __init__(self, customer, coffee, price):
        
        from customer import Customer
        from coffee import Coffee

        if not isinstance(customer, Customer):
            raise TypeError("Order.customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("Order.coffee must be a Coffee instance")
        
        if not (isinstance(price, (int, float))):
            raise TypeError("Order.price must be a number")
        price = float(price)
        if price < 1.0 or price > 10.0:
            raise ValueError("Order.price must be between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = price

        Order.all.append(self)

    def __repr__(self):
        return f"<Order customer={self.customer.name!r} coffee={self.coffee.name!r} price={self.price}>"

    
    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        from customer import Customer
        if not isinstance(value, Customer):
            raise TypeError("Order.customer must be a Customer instance")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee
        if not isinstance(value, Coffee):
            raise TypeError("Order.coffee must be a Coffee instance")
        self._coffee = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not (isinstance(value, (int, float))):
            raise TypeError("Order.price must be a number")
        value = float(value)
        if value < 1.0 or value > 10.0:
            raise ValueError("Order.price must be between 1.0 and 10.0")
        self._price = value