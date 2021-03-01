import abc


class AbsFactory(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_economy(self):
        pass

    @abc.abstractmethod
    def create_sport(self):
        pass

    @abc.abstractmethod
    def create_luxury(self):
        pass
