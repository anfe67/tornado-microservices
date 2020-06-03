class BooksFile:
        def __init__(self):
                self.books_file = "mybooksfile.txt" 
        
        def read_file(self): 
                # Liste de dictionnaires... 
                books =[] 
                # Open file 
                booksfile = open(self.books_file) 
                
                while 1: 
                        book = dict()
                        line = booksfile.readline() 
                        
                        if not line:
                                break
                        
                        # Remove all whitespaces
                        line=line.strip()
                        
                        keys_values=line.split(":::") 
                        # 4 Values are expected - title:title:author:author 
                        book[keys_values[0]] = keys_values[1]
                        book[keys_values[2]] = keys_values[3]
                        books.append(book) 
                
                booksfile.close() 
                return books 

        def write_file(self, books): 
                
                book={}
                # Open file for Writing 
                booksfile = open(self.books_file, "w")
                
                for i in range(len(books)) :
                        book=books[i]
                        line = "Author:::" + book["Author"] + ":::Title:::" +book["Title"] #+"\n"
                        print(line, file=booksfile)
                        # booksfile.write(line)
                booksfile.close()