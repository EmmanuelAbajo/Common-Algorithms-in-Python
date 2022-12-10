from abc import ABC, abstractmethod
from typing import Any

# Interface
class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass

# Abstract class
class Publication(ABC):
    def __init__(self, title) -> None:
        self.title = title

    @abstractmethod
    def printTitle(self):
        pass


class Book(Publication, JSONify):
    BOOK_TYPES = ('HARDCOVER', 'EBOOK')

    # Private variable
    __book_list = None

    def __init__(self, title, price) -> None:
        super().__init__(title)
        self.price = price

    def __repr__(self) -> str:
        return f'title={self.title} price={self.price}'   

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Book):
            raise ValueError("Can't compare book with non-book type")

        return self.title == __o.title and self.price == __o.price

    def __ge__(self, __o: object) -> bool:
        if not isinstance(__o, Book):
            raise ValueError("Can't compare book with non-book type")

        return self.price >= __o.price

    def __lt__(self, __o: object) -> bool:
        if not isinstance(__o, Book):
            raise ValueError("Can't compare book with non-book type")

        return self.price < __o.price    

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == 'price':
            if type(__value) is not float:
                raise ValueError('Price must be a float')
                
        return super().__setattr__(__name, __value)

    @classmethod
    def getBookTypes(cls):
        return cls.BOOK_TYPES

    @staticmethod
    def getBookList() -> list:
        if Book.__book_list == None:
            Book.__book_list = []
        return Book.__book_list    

    
    def printTitle(self) -> None:
        print(self.title)

    def setDiscount(self, amount) -> None:
        self._discount = amount

    def getPrice(self) -> float:
        if hasattr(self, '_discount'):
            return self.price - (self.price * self._discount)
        return self.price

    def toJSON(self):    
        pass

b1 = Book("Aphesis", 10.95)
b1.printTitle()

print(isinstance(b1, Book))
print(Book.getBookTypes())
print(repr(b1))