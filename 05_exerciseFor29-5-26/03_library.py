class Book:
    def __init__(self, title, author, publisher, purchasePrice):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.__purchasePrice = purchasePrice  # Store the purchase price
        
    def getPurchasePrice(self):
        return self.__purchasePrice
        
    def setPurchasePrice(self, newPrice):
        self.__purchasePrice = newPrice

class Catalog:
    def __init__(self, name, description, books):
        self.name = name
        self.description = description
        self.books = books
        self.setTotalValue()  # Just call the method, it handles the assignment
    
    def __eq__(self, other):
        if isinstance(other, Catalog):
            if(self.name == other.name and 
               self.description == other.description and 
               self.books == other.books):
                return True
            else:
                return False
        else:
            return False
    
    def __add__(self, other):
        if isinstance(other, Catalog):
            newName = self.name + "+" + other.name
            newDescription = self.description + other.description
            newBooks = self.books + other.books
            newCatalog = Catalog(newName, newDescription, newBooks)
            return newCatalog  # Moved inside the if block
        # You might want to raise an error or return NotImplemented here
        
    def getTotalValue(self):
        return self.__totalValue
    
    def setTotalValue(self):
        totalPrice = 0
        for book in self.books:
            totalPrice += book.getPurchasePrice()
        self.__totalValue = totalPrice
        return totalPrice
    
    def addBook(self, book):
        self.books.append(book)
        self.setTotalValue()  
    
    def removeBook(self, book):
        if book in self.books:
            self.books.remove(book)
            self.setTotalValue()


books = [
    Book("Book1", "Author1", "Publisher1", 99),
    Book("Book2", "Author2", "Publisher2", 50),
]

cat = Catalog("name", "description", books)
print(f"Total value: {cat.getTotalValue()}")

cat.addBook(Book("Book3", "Author3", "Publisher3", 25))
print(f"Total value after adding: {cat.getTotalValue()}")