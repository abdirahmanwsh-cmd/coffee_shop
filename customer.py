class Customer:
    """Customer class for the coffee shop domain.

    - name: string between 1 and 15 characters
    - class-level behaviour uses Order.all as single source of truth
    """

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"<Customer name={self.name!r}>"

    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string")
        value = value.strip()
        if len(value) < 1 or len(value) > 15:
            raise ValueError("Customer name must be between 1 and 15 characters")
        self._name = value

    
    def orders(self):
        from order import Order
        return [o for o in Order.all if o.customer is self]

    def coffees(self):
        
        return list({o.coffee for o in self.orders()})

    def create_order(self, coffee, price):
        from order import Order
        
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        """Return the Customer who spent the most total money on the given coffee.

        If no orders exist for that coffee, return None.
        """
        from order import Order
        
        coffee_orders = [o for o in Order.all if o.coffee is coffee]
        if not coffee_orders:
            return None
    
        totals = {}
        for o in coffee_orders:
            totals[o.customer] = totals.get(o.customer, 0.0) + o.price

        best = max(totals.items(), key=lambda kv: kv[1])[0]
        return best