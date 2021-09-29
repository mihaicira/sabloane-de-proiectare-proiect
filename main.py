class Book:
    content = []
    def __init__(self,titlu):
        self.titlu = titlu

    def createNewParagraph(self,paragraph):
        self.content.append(paragraph)

    def createNewImage(self,image):
        self.content.append(image)

    def createNewTable(self,table):
        self.content.append(table)

    def print(self):
        for items in self.content:
            print(items)


if __name__ == "__main__":
    book = Book("Disco Titanic")
    book.createNewParagraph("Paragraph 1")
    book.createNewParagraph("Paragraph 2")
    book.createNewParagraph("Paragraph 3")
    book.createNewImage("Image 1")
    book.createNewParagraph("Paragraph 4")
    book.createNewTable("Table 1")

    book.print()