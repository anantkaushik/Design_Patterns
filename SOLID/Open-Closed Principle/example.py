"""
Let’s imagine you have a store, and you give a discount of 10% to your regular customers.
When you decide to offer double the 20% discount to VIP customers. You may modify the class like this:
"""


class Discount:
    def __init__(self, customer_type, price):
        self.customer_type = customer_type
        self.price = price

    def give_discount(self):
        if self.customer_type == 'regular':
            return self.price * 0.1
        # This fails the OCP principle. If we want to give a new percent discount to a different
        # type of customers, new logic will be added.
        if self.customer_type == 'vip':
            return self.price * 0.2


# Correct Implementation
class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        pass


# Here we don't need to update the class.
# We can just extend the base class and implement it's functionality/logic.
class RegularDiscount(Discount):
    def get_discount(self):
        return self.price * 0.1


class VIPDiscount(Discount):
    def get_discount(self):
        return self.price * 0.2
