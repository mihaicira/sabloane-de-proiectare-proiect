from Element import Element

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
