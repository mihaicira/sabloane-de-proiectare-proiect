from Element import Element
import time
import abc

class Picture(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def url(self):
        pass

    @abc.abstractmethod
    def dim(self):
        pass

    @abc.abstractmethod
    def content(self):
        pass

class Image(Element,Picture):
    # leaf
    def __init__(self, url):
        self.url = url
        time.sleep(2)

    def add(self, component):
        pass;

    def remove(self, component):
        pass;

    def print(self):
        print("Image with url:", self.url)

    def url(self):
        pass;

    def dim(self):
        pass

    def content(self):
        pass;

class ImageProxy(Element,Picture):
    def __init__(self, url):
        self.url = url
        self.realImage = None

    def add(self, component):
        pass;

    def remove(self, component):
        pass

    def print(self):
        self.loadImage()
        self.realImage.print()
        pass

    def url(self):
        pass;

    def dim(self):
        pass

    def content(self):
        pass;

    def loadImage(self):
        if(self.realImage == None):
            self.realImage = Image(self.url)

