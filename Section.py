from Element import Element

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

