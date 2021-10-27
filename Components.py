import abc

class Element(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add(self, component):
        pass
        # self._children.add(component)

    @abc.abstractmethod
    def remove(self, component):
        pass
        # self._children.discard(component)

    @abc.abstractmethod
    def print(self):
        pass
        # print(self._children)

class Section(Element):
    #implements interface Element
    def __init__(self,title):
        self.title = title
        self._children = set()

    def add(self, component):
        self._children.add(component)

    def remove(self, component):
        self._children.discard(component)

    def print(self):
        print(self.title)
        for child in self._children:
            child.print()

class Book(Section):
    #inherits class Section
    def __init__(self,title):
        Section.__init__(self,title)
        self.authors = []

    def add(self, component):
        self._children.add(component)

    def remove(self, component):
        self._children.discard(component)

    def addAuthor(self,name):
        self.authors.append(name)

    def print(self):
        print(f"Title: {self.title}")
        print("\nAuthor(s):")
        for author in self.authors:
            author.print()
        print()
        for child in self._children:
            child.print()

class Paragraph(Element):
    #leaf
    def __init__(self,content):
        self.content = content

    def add(self, component):
        pass;

    def remove(self, component):
        pass;

    def print(self):
        print(self.content)

class Image(Element):
    # leaf
    def __init__(self, link):
        self.link = link

    def add(self, component):
        pass;

    def remove(self, component):
        pass;

    def print(self):
        print(self.link)

class Table(Element):
    # leaf
    def __init__(self, content):
        self.link = content

    def add(self, component):
        pass;

    def remove(self, component):
        pass;

    def print(self):
        print(self.content)
