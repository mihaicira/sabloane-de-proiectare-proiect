from Author import *
from Element import *
from Section import *
from Book import *
from Image import *
from Table import *
from Paragraph import *
from BookManager import *
from Visitor import *

def Printing():
   Manager.getInstance().getBook().print()

if __name__ == "__main__":
   cap1 = Section("Capitolul 1")
   p1 = Paragraph("Paragraph 1")
   cap1.add(p1)
   p2 = Paragraph("Paragraph 2")
   cap1.add(p2)
   p3 = Paragraph("Paragraph 3")
   cap1.add(p3)
   p4 = Paragraph("Paragraph 4")
   cap1.add(p4)

   cap1.add(ImageProxy("Image One"))
   cap1.add(Image("Image Two"))
   cap1.add(Paragraph("Some text"))
   cap1.add(Table("Table 1"))

   cap2 = Section("Chapter 2")
   cap2_1 = Section("Chapter 2.1")
   cap2_1.add(Paragraph("Paragraph 1 from c2"))
   cap2.add(cap2_1)


   stats = BookStatistics()
   cap1.accept(stats)
   stats.printStatistics()


   book = Book("My book")
   book.add(cap1)
   book.add(cap2)

   toc = GenerateToC()
   book.accept(toc)
   toc.getToC()