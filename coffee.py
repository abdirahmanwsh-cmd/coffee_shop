class Coffee:
    """Coffee class for the coffee shop domain.

    - name: string at least 3 characters
    """

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"<Coffee name={self.name!r}>"

    # name property with validation
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string")
        value = value.strip()
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters")
        self._name = value

    # relationship methods
    def orders(self):
        from order import Order
        return [o for o in Order.all if o.coffee is self]

    def customers(self):
        return list({o.customer for o in self.orders()})

    # aggregate/association methods
    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0.0
        total = sum(o.price for o in orders)
        return total / len(orders)