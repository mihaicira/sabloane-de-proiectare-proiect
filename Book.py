from Components import Chapter
class Book:
    def __init__(self,title):
        self.title = title
        self.authors = []
        self.chapters = []


    def addAuthor(self,name):
        self.authors.append(name)

    def createChapter(self,title):
        newChapter = Chapter(title)
        self.chapters.append(newChapter)
        return len(self.chapters)-1

    def getChapter(self,id):
        return self.chapters[id]


    def print(self):
        print(f"==================Book: {self.title}==================")
        print("======Author(s)======")
        if(not len(self.authors)):
            print("None")
        else:
            for author in self.authors:
                author.print()

        print("======Content======")

        if (not len(self.chapters)):
            print("empty book")
            return;

        for item in self.chapters:
            item.print()