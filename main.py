from Author import Author
from Element import Element
from Section import Section
from Book import Book
from Image import *
from Table import Table
from Paragraph import Paragraph
import time

if __name__ == "__main__":

    start = time.time()
    img1 = ImageProxy("Pamela Anderson")
    img2 = ImageProxy("Kim Kardashian")
    img3 = ImageProxy("Kirby Griffin")

    playboyS1 = Section("Front Cover")
    playboyS1.add(img1)

    playboyS2 = Section("Summer Girls")
    playboyS2.add(img2)
    playboyS2.add(img3)

    playboy = Book("Playboy")

    playboy.add(playboyS1)
    playboy.add(playboyS2)
    end = time.time()
    print("creation of content (time): ",end - start)

    start = time.time()
    playboyS1.print()
    end = time.time()
    print("printing section 1 (time): ", end - start)

    start = time.time()
    playboyS1.print()
    end = time.time()
    print("printing section 1 again (time): ", end - start)
