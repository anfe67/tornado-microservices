import tornado.web
import book
import json

class AddHandler(tornado.web.RequestHandler):
    def initialize(self, books):
        self.books = books
        
    def post(self):
        
        title = self.get_argument('title').strip()
        author = self.get_argument('author').strip()
        
        result = self.books.add_book(title, author)
        
        if result == False: 
            self.set_status(200)
            self.write(json.dumps("Book already Exists"))
        else :
            self.set_status(201)
            self.write(json.dumps(result))