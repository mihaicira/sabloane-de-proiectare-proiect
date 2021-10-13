from Book import Book
from Author import Author
from Components import *

if __name__ == "__main__":
    book = Book("Disco Titanic")
    author = Author("Jennifer Lopez")

    #add author
    book.addAuthor(author)

    #add first chapter
    idxChapterOne = book.createChapter("Chapter One")

    #get first chapter
    chp1 = book.getChapter(idxChapterOne)

    #add first sub sub chapter
    idxSubchapterOneOne = chp1.createSubChapter("Subchapter 1.1")

    #get first sub sub chapter
    subChapterOneOne = chp1.getSubChapter(idxSubchapterOneOne)

    #add content
    subChapterOneOne.createNewParagraph("Paragraph 1")
    subChapterOneOne.createNewParagraph("Paragraph 2")
    subChapterOneOne.createNewParagraph("Paragraph 3")
    subChapterOneOne.createNewImage("Image 1")
    subChapterOneOne.createNewParagraph("Paragraph 4")
    subChapterOneOne.createNewTable("Table 1")

    #########
    book.print()