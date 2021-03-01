from Abstract_Factory.Example.factories.ford_factory import FordFactory
from Abstract_Factory.Example.factories.gm_factory import GMFactory

for factory in [FordFactory, GMFactory]:
    factory = factory()

    car = factory.create_economy()
    car.start()
    car.stop()

    car = factory.create_sport()
    car.start()
    car.stop()

    car = factory.create_luxury()
    car.start()
    car.stop()
