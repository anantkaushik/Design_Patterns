from abs_factory import AbsFactory
from Factory.Example.autos.nullcar import NullCar


class NullFactory(AbsFactory):

    def create_auto(self):
        self.null_car = null_car = NullCar()
        null_car.name = "Unknown"
        return null_car
