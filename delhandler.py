import tornado.web
import book
import json

class DelHandler(tornado.web.RequestHandler):
    def initialize(self, books):
        self.books = books
    def delete(self):
        title = self.get_argument('title')
        result = self.books.del_book(title)
        if result:
            self.write("Deleted book title: {0} successfully".format(title))
        else:
            self.write("Book '{0}' not found".format(title))
            
        self.set_status(200)