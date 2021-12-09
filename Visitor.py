import abc
from Author import *
from Element import *
from Section import *
from Book import *
from Image import *
from Table import *
from Paragraph import *
from TableOfContents import *
from BookManager import *

class Visitor(metaclass=abc.ABCMeta):
    def visit(self,obj):
        self.obj = obj;


class BookStatistics(Visitor):
    def __init__(self):
        self.obj = None

    def visit(self,obj):
        self.obj = obj;
        if(str(type(obj)).split('.')[1].split("'")[0] == "Section"):
            self.obj.content = self.obj.title

    def printStatistics(self):
        stats = {}
        for child in self.obj._children:
            obj_type = str(type(child)).split('.')[1].split("'")[0]

            if(obj_type in stats):
                stats[obj_type] += 1
            else:
                stats[obj_type] = 1

        print(f"{self.obj.title}'s statistics: ")
        for key in stats:
            print(f"*** Number of {key}(s):  {stats[key]}");


class RenderContentVisitor(Visitor):
    def __init__(self):
        self.obj = None

    def renderContent(self):
        for child in self.obj._children:
            child.print()

class GenerateToC(Visitor):
    def __init__(self):
        self.obj = None

    def getToC(self):
        print(f"{self.obj.title}'s table of contents: ")
        print(TableOfContents(self.obj).getToc())