from Element import Element
import abc

class Paragraph(Element):
    #leaf
    def __init__(self,content):
        self.content = content
        self.alignmentStrategy = AlignLeft()

    def add(self, component):
        pass;

    def remove(self, component):
        pass;

    def print(self):
        print("Paragraph:",self.alignmentStrategy.render(self.content))

    def setAlignStrategy(self,strategy):
        self.alignmentStrategy = strategy

class AlignStrategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def render(self, text):
        pass

class AlignLeft(AlignStrategy):
    def render(self,text):
        return "##"+text

class AlignCenter(AlignStrategy):
    def render(self,text):
        return "##"+text+"##"

class AlignRight(AlignStrategy):
    def render(self,text):
        return text+"##"

