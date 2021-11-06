#Lab05
#Nealson Setiawan

class Book:

    def __init__(self,title = "", author = "", year = None):
        self.title = title
        self.author = author
        self.year = year

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getYear(self):
        return self.year

    def getBookDetails(self):
        return "Title: {}, Author: {}, Year: {}".format(self.getTitle(),self.getAuthor(),\
            self.getYear())
    
    def __gt__(self,rhs):
        if self.getAuthor().lower() > rhs.getAuthor().lower():
            return True
        elif self.getAuthor().lower() < rhs.getAuthor().lower():
            return False
        else:   
            if self.getYear() > rhs.getYear():
                return True
            elif self.getYear() < rhs.getYear():
                return False
            else:
                if self.getTitle().lower() > rhs.getTitle().lower():
                    return True
                elif self.getTitle().lower() < rhs.getTitle().lower():
                    return False
                else:
                    return False
