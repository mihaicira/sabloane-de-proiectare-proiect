import abc

class Element(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add(self, component):
        pass

    @abc.abstractmethod
    def remove(self, component):
        pass

    @abc.abstractmethod
    def print(self):
        pass

    def accept(self,visitor):
        visitor.visit(self)


