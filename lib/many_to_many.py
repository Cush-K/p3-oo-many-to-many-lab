class Author:
    all = []
    
    def __init__(self, name):
        self.name = name
        Author.all.append(self)
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        if isinstance(book, Book):
            contract = Contract(self, book, date, royalties)
            return contract
        else:
            raise Exception("Book must be an instance of the Book Class")
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

class Book:
    all = []
    
    def __init__(self, title):
        self.title = title
        Book.all.append(self)
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]
    
        

class Contract:
    all = []
        
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class")
        
        self.book = book
        self.author = author
        if isinstance(date, str):
            self.date = date
        else:
            raise Exception("The date should be a String")
        if isinstance(royalties, int):
            self.royalties = royalties
        else:
            raise Exception("Royalties should be an Integer")
                         
        Contract.all.append(self)
        
    
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]




author1 = Author("Mwas")
author2 = Author("Jack")

book1 = Book("Book Two")
book2 = Book("Book One")

contract1 = author1.sign_contract(book1, "2024-09-01", 10)
contract2 = author2.sign_contract(book2, "2024-09-02", 15)


[print(book.title) for book in author1.books()]
print(contract2.author.name)
print(author2.total_royalties())
[print(contract.author.name) for contract in author1.contracts()]