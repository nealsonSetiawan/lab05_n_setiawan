#BookCollection 
from BookCollectionNode import BookCollectionNode

class BookCollection:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def getNumberOfBooks(self):
        c = 0 #counter
        current = self.head

        while(current != None):
            c = c + 1
            current = current.getNext()

        return c

    def remove(self,item):
        current = self.head
        previous = None
        found = False

        while(not found):
            if current.getData() == item:
                found = True

            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()

        else:
            previous = previous.setNext(current.getNext())

    def insertBook(self,item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = BookCollectionNode(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def getBooksByAuthor(self,author):
        current = self.head
        strTotal = ""
        strIndividual = ""
        author = author.lower()

        while(current != None):
                cData = current.getData()
                if(cData.getAuthor().lower() == author):
                    strIndividual = "Title: {}, Author: {}, Year: {}".format(cData.getTitle(),cData.getAuthor(),\
                        cData.getYear())
                    strTotal = strTotal + strIndividual + "\n"
                current = current.getNext() 

        return strTotal


    def getAllBooksInCollection(self):
        current = self.head
        strTotal = ""
        strIndividual = ""

        while(current != None):
                cData = current.getData()
                strIndividual = "Title: {}, Author: {}, Year: {}".format(cData.getTitle(),cData.getAuthor(),\
                    cData.getYear())
                strTotal = strTotal + strIndividual + "\n"
                current = current.getNext() 

        return strTotal

'''            cData = current.getData()
            strIndividual = "Title: {}, Author: {}, Year: {}".format(cData.getTitle(),cData.getAuthor(),\
                cData.getYear())
            strTotal = strTotal + strIndividual   '''


'''
    def getBooksByAuthor(self,author):
        author = author.lower()
        
        current = self.head
        str = ""

        if current == None:
            return ""
        else:
            if(current.getData().getAuthor().lower() == author):
                cData = current.getData()
                str = "Title: {}, Author: {}, Year: {}\n".format(cData.getTitle(),cData.getAuthor(),\
                    cData.getYear())
            self.head = current.getNext()
            return str + (self.getBooksByAuthor(author))
            '''