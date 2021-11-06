from Book import Book
from BookCollection import BookCollection
from BookCollectionNode import BookCollectionNode


def test_BookCollection(): #Tests for the BookCollection Class
    bc1 = BookCollection()
    b1 = Book("The Shining","Stephen King", 1981)
    b2 = Book("The Shining","Stephen King", 1980)
    b3 = Book("The Shining","Bephen Ping", 1980)
    bc1.insertBook(b1)
    bc1.insertBook(b2)
    bc1.insertBook(b3)
    assert (bc1.getAllBooksInCollection()) == "Title: The Shining, Author: Bephen Ping, Year: 1980\n" + \
        "Title: The Shining, Author: Stephen King, Year: 1980\n" + \
            "Title: The Shining, Author: Stephen King, Year: 1981\n"
    assert bc1.getBooksByAuthor("") == ""
    assert bc1.isEmpty() == False
    assert bc1.getNumberOfBooks() == 3

    #Empty Book Insertion
    bEmpty = Book()
    bc1.insertBook(bEmpty)
    assert bc1.getAllBooksInCollection() == "Title: , Author: , Year: None\n" + \
        "Title: The Shining, Author: Bephen Ping, Year: 1980\n" + \
            "Title: The Shining, Author: Stephen King, Year: 1980\n" + \
                "Title: The Shining, Author: Stephen King, Year: 1981\n"
    assert bc1.isEmpty() == False
    assert bc1.getNumberOfBooks() == 4
    assert bc1.getBooksByAuthor("") == "Title: , Author: , Year: None\n"
    assert bc1.getBooksByAuthor("Stephen King") == "Title: The Shining, Author: Stephen King, Year: 1980\n" + \
                "Title: The Shining, Author: Stephen King, Year: 1981\n"

    #Empty Book Collection
    bc1.remove(b1)
    bc1.remove(b2)
    bc1.remove(b3)
    bc1.remove(bEmpty)

    assert bc1.getNumberOfBooks() == 0
    assert bc1.getBooksByAuthor("KING, STEPHEN") == ""
    assert bc1.isEmpty() == True
    assert (bc1.getAllBooksInCollection()) == ""

def test_Book(): #Tests for Book class
    bEmpty = Book()
    b1 = Book("The Shining","Stephen King", 1981)

    assert bEmpty.getAuthor() == ""
    assert bEmpty.getTitle() == ""
    assert bEmpty.getYear() == None

    assert b1.getTitle() == "The Shining"
    assert b1.getAuthor() == "Stephen King"
    assert b1.getYear() == 1981

def test_BookCollectionNode(): #Tests for the BookCollectionNode class
    b1 = Book("The Shining","Stephen King", 1981)
    b2 = Book("The Shining","Stephen King", 1980)

    b1Node = BookCollectionNode(b1)
    assert b1Node.getData() == b1
    assert b1Node.getNext() == None

    b1Node.setData(b2) == b2
    assert b1Node.getData() == b2
    
    b2Node = BookCollectionNode(b2)
    b1Node.setNext(b2Node)
    assert b1Node.getNext() == b2Node


def prof_test_BookCollection(): #Professor Tests for the Book Collection class
    bEmpty = Book()
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)

    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)

    print(bc.getAllBooksInCollection())
    print("---")
    print(bc.getBooksByAuthor("KING, Stephen"))


test_BookCollection()
test_Book()
test_BookCollectionNode()
prof_test_BookCollection()