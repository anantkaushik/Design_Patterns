from Abstract_Factory.Example.factories.abs_factory import AbsFactory
from Abstract_Factory.Example.autos.ford import FordMustang, FordFiesta, LincolnMKS


class FordFactory(AbsFactory):

    def create_economy(self):
        return FordFiesta()

    def create_sport(self):
        return FordMustang()

    def create_luxury(self):
        return LincolnMKS()
