class Machine:
    def print(self, document):
        raise NotImplementedError()

    def fax(self, document):
        raise NotImplementedError()

    def scan(self, document):
        raise NotImplementedError()


# ok if you need a multifunction device
class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


# Machine Interface is not ok here.
# As in OldFashionedPrinter we don't have
# fax and scan functionality.
class OldFashionedPrinter(Machine):
    def print(self, document):
        # ok - print stuff
        pass

    def fax(self, document):
        pass  # do-nothing

    def scan(self, document):
        """Not supported!"""
        raise NotImplementedError('Printer cannot scan!')
