from Element import Element

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

