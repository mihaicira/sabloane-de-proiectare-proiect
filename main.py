from Author import Author
from Components import *

if __name__ == "__main__":
    book = Book("Disco Titanic")
    author = Author("Radu Pavel Gheo")

    #add author
    book.addAuthor(author)

    #add content
    cap1 = Section("Capitolul 1")
    # a = Section('b')

    # cap11 = Section("Capitolul 1.1")
    # cap111 = Section("Capitolul 1.1.1")
    # cap1.add(cap11)
    # cap11.add(cap111)

    book.add(Paragraph("Multumesc celor care..."))
    book.add(cap1)

    ######
    book.print()






    #get first chapter
    # chp1 = book.getChapter(idxChapterOne)

    #add first sub sub chapter
    # idxSubchapterOneOne = chp1.createSubChapter("Subchapter 1.1")

    #get first sub sub chapter
    # subChapterOneOne = chp1.getSubChapter(idxSubchapterOneOne)

    #add content
    # subChapterOneOne.createNewParagraph("Paragraph 1")
    # subChapterOneOne.createNewParagraph("Paragraph 2")
    # subChapterOneOne.createNewParagraph("Paragraph 3")
    # subChapterOneOne.createNewImage("Image 1")
    # subChapterOneOne.createNewParagraph("Paragraph 4")
    # subChapterOneOne.createNewTable("Table 1")

    #########
    # book.print()