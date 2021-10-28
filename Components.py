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

class Section(Element):
    #implements interface Element
    def __init__(self,title):
        self.title = title
        self._children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

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
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def addAuthor(self,name):
        self.authors.append(name)

    def print(self):
        print(f"Book: {self.title}")
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
        print("Paragraph:",self.content)

class Image(Element):
    # leaf
    def __init__(self, link):
        self.link = link

    def add(self, component):
        pass;

    def remove(self, component):
        pass;

    def print(self):
        print("Image with name:",self.link)

class Table(Element):
    # leaf
    def __init__(self, content):
        self.link = content

    def add(self, component):
        pass;

    def remove(self, component):
        pass;

    def print(self):
        print("Table:",self.content)
