#Bookshelf problem

class Book:

    def __init__(self, iID, iW):
       self.id = iID
       self.width = iW

    def __str__(self):
        return str(self.id)

    def getWidth(self):
        return self.width

    def getID(self):
        return self.id

class Shelf:

    def __init__(self, iW):
        self.width = iW
        self.books = []

    def bookTotal(self):
        t = 0
        for i in range(len(self.books)):
            endTerm = self.books.pop(i)
            self.books.insert(i, endTerm)
            endWidth = endTerm.getWidth()
            t = t + endWidth
        return t
    
    def add(self, abook):
        self.books.insert(0,abook)
        while self.width < self.bookTotal():
            self.books.pop()

    def remove(self, abookID):
        i = 0
        while self.books[i].getID() != abookID:
           i = i + 1
        self.books.pop(i)
        
    def __str__(self):
        printbook = ""
        for i in range(len(self.books)):
            book = self.books.pop(i)
            self.books.insert(i,book)
            bookID = book.getID()
            printbook = printbook + str(bookID) + "  "
        return printbook

def main():

    width = int(input("How wide is your bookshelf "))
    bookshelf = Shelf(width)
    
    command = input("Input a command ")
    while command != "Quit":
        clist = command.split()
        if clist[0] == "A":
            nameOfBook = int(clist[1])
            widthOfBook = int(clist[2])
            
            abook = Book(nameOfBook,widthOfBook)
            bookshelf.add(abook)
        else:
            if clist[0] == "R":
                nameOfBook = int(clist[1])
                
                bookshelf.remove(nameOfBook)
            else:
                print("BAD Command...try again")

        command = input("Input a command ")

    print(bookshelf)
   
main()
