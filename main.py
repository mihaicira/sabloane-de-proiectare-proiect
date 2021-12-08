from Author import *
from Element import *
from Section import *
from Book import *
from Image import *
from Table import *
from Paragraph import *
from BookManager import *
import time

def Printing():
   Manager.getInstance().getBook().print()

if __name__ == "__main__":

   myBook = Book("My Book")
   Manager = BookManager()

   Manager.getInstance().setBook(myBook)

   auth = Author("Myself")
   myBook.addAuthor(auth)

   cap1 = Section("capitolul 1")
   p1 = Paragraph("Paragraph 1")
   cap1.add(p1)
   p2 = Paragraph("Paragraph 2")
   cap1.add(p2)
   p3 = Paragraph("Paragraph 3")
   cap1.add(p3)
   p4 = Paragraph("Paragraph 4")
   cap1.add(p4)
   print("--without alignment:")
   cap1.print()

   p1.setAlignStrategy(AlignCenter())
   p2.setAlignStrategy(AlignRight())
   p3.setAlignStrategy(AlignLeft())

   print("\n--with alignment:")
   cap1.print()

   Printing()