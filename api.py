# ORIGIN: Python Rest API Example - Bill Ward . DZONE

import tornado.ioloop
import tornado.web
from addhandler import AddHandler
from delhandler import DelHandler
from gethandler import GetHandler
from infohandler import InfoHandler
from errorhandler import ErrorHandler
from detailshandler import DetailsHandler
from book import Books 

myBooks = Books()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Book Microservice v1</h1>")

def make_app():
   
    return tornado.web.Application([
        (r"/books", MainHandler),                                  
        (r"/books/info", InfoHandler),                             
        (r"/books/addbook", AddHandler, dict(books = myBooks)),
        (r"/books/delbook", DelHandler, dict(books = myBooks)),
        (r"/books/listbooks", GetHandler, dict(books = myBooks)),
        (r"/books/bookdetails", DetailsHandler, dict(books = myBooks)),
        (r"/", ErrorHandler)
    ])
if __name__ == "__main__":
    # READ BOOKS 
    myBooks.books = Books.read_books_from_file()
    app = make_app()
    
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()    
    
# Appelles API: 
# http://localhost:8888/books
# http://localhost:8888/books/info
# http://localhost:8888/books/addbook?title="How to Make a Million Dollars Blogging"&author="Bill Ward"
# http://localhost:8888/books/delbook?title="How to Make a Million Dollars Blogging"
# http://localhost:8888/books/listbooks
# http://localhost:8888/books/listbooks?author="Bill Ward"
# http://localhost:8888/books/bookdetails?title="Title"</b> - Api to produce HTML for the book with title

# Problemes avec cette solution de base :
# Requetes pas du bon type !
# Gestion des erreurs et des reponses pas standard ! 