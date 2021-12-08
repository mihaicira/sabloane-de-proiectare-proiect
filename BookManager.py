class BookManager():
    def __init__(cls):
        cls._instance = None

    def getInstance(cls):
        return cls;

    def setBook(cls,book):
        if(cls._instance is None):
            cls._instance = book
        return cls._instance

    def getBook(cls):
        return cls._instance
