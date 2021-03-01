from Abstract_Factory.Example.factories.abs_factory import AbsFactory
from Abstract_Factory.Example.autos.gm import ChevySpark, ChevyCamaro, CadillacCTS


class GMFactory(AbsFactory):

    def create_economy(self):
        return ChevySpark()

    def create_sport(self):
        return ChevyCamaro()

    def create_luxury(self):
        return CadillacCTS()
