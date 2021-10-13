class Chapter:
    def __init__(self,title):
        self.title = title
        self.subchapters = []

    def createSubChapter(self,title):
        newSubChapter = SubChapter(title)
        self.subchapters.append(newSubChapter)
        return len(self.subchapters)-1

    def getSubChapter(self,id):
        return self.subchapters[id]

    def print(self):
        print(f"[Chapter] {self.title}")
        if (not len(self.subchapters)):
            print("empty chapter")
            return;

        for item in self.subchapters:
            item.print()

class SubChapter:
    def __init__(self, title):
        self.title = title
        self.content = []

    def createNewParagraph(self,text):
        newParagraph = Paragraph(text)
        self.content.append(newParagraph)

    def createNewImage(self,imageName):
        newImage = Image(imageName)
        self.content.append(newImage)

    def createNewTable(self,title):
        newTable = Table(title)
        self.content.append(newTable)

    def print(self):
        print(f"[SubChapter] {self.title}")

        if(not len(self.content)):
            print("empty subchapter")
            return;

        for item in self.content:
            item.print()

class Image:
    def __init__(self, imageName):
        self.imageName = imageName

    def print(self):
        print(f"[Image] {self.imageName}")

class Paragraph:
    def __init__(self, text):
        self.text = text

    def print(self):
        print(f"[Paragraph] {self.text}")

class Table:
    def __init__(self, title):
        self.title = title

    def print(self):
        print(f"[Table] {self.title}")

class TableOfContents:
    def __init__(self):
        self.to_be_continued = "to_be_continued"