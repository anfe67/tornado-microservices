import json
from booksfile import BooksFile 

myBooksFile = BooksFile() 

class Books:
    def __init__(self):
        self.books = []
        
    def read_books_from_file():
        return myBooksFile.read_file()
    
    def write_books_to_file(self, file):
        myBooksFile.write_file(self, self.books)
        return None
        
    def find_book(self, author, title): 
        for book in self.books: 
            if book["Author"]==author and book["Title"]==title :
                return True       
        return False   
    
    def add_book(self, title, author):
        # IF IT EXISTS, SHOULD NOT BE ADDED! 
        if not self.find_book(author, title):        
            new_book = {}
            new_book["Title"] = title
            new_book["Author"] = author
            
            self.books.append(new_book)
            # DEBUG print("Book: {0}".format(new_book))
            # WRITE BOOKS FILE
            myBooksFile.write_file(self.books)
            return json.dumps(new_book)
        else : 
            return False

        
    def del_book(self, title):
        found = False
        for idx, book in enumerate(self.books):
            print("Book: ", book["Title"] , "Input: ", title)
            if book["Title"] == title:
                found = True
                del self.books[idx] # Alternative to remove and pop
        print("DEBUG books: {0}".format(json.dumps(self.books)))
        # WRITE BOOKS FILE 
        myBooksFile.write_file(self.books)
        return found
    
    def get_all_books(self):
        return self.books
    def json_list(self):
        return json.dumps(self.books)
    
    def get_books_from_author(self, author):
        books_author = []
        for book in self.books: 
            if book["Author"]==author: 
                books_author.append(book)
        
        if len(books_author)==0: 
            return None
        else: 
            return json.dumps(books_author)
                
    def get_book_with_title(self, title):
        books_title= []
        for book in self.books: 
            if book["Title"]==title: 
                books_title.append(book) 
        if len(books_title)==0: 
            return None
        else: 
            return books_title
        