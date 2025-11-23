#  Coffee Shop Domain Modeling

A Python object‑oriented programming project modeling the relationships between **Customers**, **Coffees**, and **Orders**. This assessment demonstrates your ability to design classes, implement relationships, enforce validations, and compute aggregate behaviors across a small domain model.

---

##  Project Overview

This project implements a simplified domain model of a coffee shop with the following entities:

* **Customer** – A person who buys coffee.
* **Coffee** – A type of coffee sold at the shop.
* **Order** – Represents a purchase made by a customer for a specific coffee.

### Relationship Rules

* A **Customer** can have many **Orders**.
* A **Coffee** can have many **Orders**.
* An **Order** belongs to exactly **one Customer** and **one Coffee**.
* Customers and Coffees have a **many‑to‑many** relationship *through Orders*.





##  Folder Structure


coffee_shop/
│
├── customer.py
├── coffee.py
├── order.py
├── debug.py
├── README.md
└── tests/
    ├── test_customer.py
    ├── test_coffee.py
    └── test_order.py




##  Installation Instructions

### 1. Clone the repository


git clone <git@github.com:abdirahmanwsh-cmd/coffee_shop.git>
cd coffee_shop


### 2. Create a virtual environment using pipenv


pipenv install
pipenv shell


### 3. Install testing dependencies


pipenv install pytest




##  Domain Model Summary

### **Customer Class**

* Stores customer name (1–15 characters)
* Methods:

  * `orders()` → All orders made by the customer
  * `coffees()` → Unique coffees ordered
  * `create_order(coffee, price)` → Creates a new order
  * `most_aficionado(coffee)` (class method) → Customer who spent the most on a coffee

### **Coffee Class**

* Stores coffee name (min 3 characters)
* Methods:

  * `orders()` → Orders containing this coffee
  * `customers()` → Unique customers who ordered it
  * `num_orders()` → Count of orders
  * `average_price()` → Average price of all orders

### **Order Class**

* Connects a Customer to a Coffee
* Validates:

  * `customer` must be a Customer instance
  * `coffee` must be a Coffee instance
  * `price` must be between 1.0 and 10.0
* All orders stored in class variable `Order.all`



##  Running Tests

To run all tests:


pytest


This project includes tests for:

* Customer behaviors
* Coffee behaviors
* Order validations and relationships



##  Debugging & Manual Testing

A `debug.py` file is included for interactive testing.
Run it with:


python debug.py


Use this file to manually create customers, coffees, and orders to test your implementation.



##  Key Features Implemented

* Class-based OOP structure
* Strong type and value validation
* Use of class-level data (`Order.all`) for global relationship tracking
* Many-to-many relationships through a join model
* Aggregate and composition methods (totals, averages, unique sets)
* Clean, readable, PEP8-compliant code
* Automated unit tests



##  Future Improvements

Possible extensions to enhance the project:

* Add timestamps to orders
* Add loyalty points for customers
* Implement a CoffeeShop class to manage menus and customers
* Add persistence using JSON or SQLite



##  Author

**Abdirahman Sheikh**

Feel free to reach out if you want help extending or improving this project on Abdirahman.wsh@gmail.com



##  License

This project is for educational use.
