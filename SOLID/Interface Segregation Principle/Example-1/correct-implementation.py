from abc import abstractmethod

# According to ISP
# Many specific interfaces are better than one
# do it all interface.
class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document): 
        pass


# same for Fax, etc.
# Here defining Printer and Scanner Interfaces separately
# we can use them separately or together according to the usecase.
class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        pass  # something meaningful
