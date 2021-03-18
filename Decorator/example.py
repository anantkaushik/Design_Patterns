from abc import ABC, abstractmethod


class AbstractCoffee(ABC):

    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_ingredients(self):
        pass

    def get_tax(self):
        return 0.1 * self.get_cost()


class ConcreteCoffee(AbstractCoffee):

    def get_cost(self):
        return 1.00

    def get_ingredients(self):
        return 'coffee'


class AbstractCoffeeDecorator(AbstractCoffee):

    def __init__(self, decorated_coffee):
        self.decorated_coffee = decorated_coffee

    def get_cost(self):
        return self.decorated_coffee.get_cost()

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients()


class Sugar(AbstractCoffeeDecorator):

    def __init__(self, decorated_coffee):
        AbstractCoffeeDecorator.__init__(self, decorated_coffee)

    def get_cost(self):
        return self.decorated_coffee.get_cost()

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ', sugar'


class Milk(AbstractCoffeeDecorator):

    def __init__(self, decorated_coffee):
        AbstractCoffeeDecorator.__init__(self, decorated_coffee)

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 0.25

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ', milk'


class Vanilla(AbstractCoffeeDecorator):

    def __init__(self, decorated_coffee):
        AbstractCoffeeDecorator.__init__(self, decorated_coffee)

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 0.75

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ', vanilla'


if __name__ == '__main__':
    myCoffee = ConcreteCoffee()
    print('Ingredients: ' + myCoffee.get_ingredients() +
          '; Cost: ' + str(myCoffee.get_cost()) + '; sales tax = ' + str(myCoffee.get_tax()))

    myCoffee = Milk(myCoffee)
    print('Ingredients: ' + myCoffee.get_ingredients() +
          '; Cost: ' + str(myCoffee.get_cost()) + '; sales tax = ' + str(myCoffee.get_tax()))

    myCoffee = Vanilla(myCoffee)
    print('Ingredients: ' + myCoffee.get_ingredients() +
          '; Cost: ' + str(myCoffee.get_cost()) + '; sales tax = ' + str(myCoffee.get_tax()))

    myCoffee = Sugar(myCoffee)
    print('Ingredients: ' + myCoffee.get_ingredients() +
          '; Cost: ' + str(myCoffee.get_cost()) + '; sales tax = ' + str(myCoffee.get_tax()))
