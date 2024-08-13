# interface segregation principle
# idea is not to stick too many methods an interface
# you shpuld split it in separate interfaces

# example adding too many functionality in a printer

from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass
    def scan(self, document):
        pass

    def fax(self, document):
        pass


class Printer:

    @abstractmethod
    def print(self, document):
        pass

class Scanner:

    @abstractmethod
    def scan(self, document):
        pass


class PhotoCopier(Printer, Scanner):
    def print(self, document):
        pass

    def scan(self, document):
        pass


class MultiFunctionPrinter(Machine, Scanner):

    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class ModernPrinter(MultiFunctionPrinter):

    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)

