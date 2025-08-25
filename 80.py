class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author
        
    @property
    def description(self):
        return self._title,self._author
    
    @description.setter
    def description(self,new_title, new_author):
        self._title = new_title
        self._author = new_author
        
    @description.deleter
    def description(self):
        del self._author,self._title
        
        
book  = Book("Harry Potter", "J.K. Rowling")
print(book.description)