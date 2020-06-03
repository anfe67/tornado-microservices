import tornado.web
import book
import json
import asyncio 

class GetHandler(tornado.web.RequestHandler):
    def initialize(self, books):
        self.books = books
        
    async def get(self):
        
        result="[]"
        
        author = self.get_argument("author", None) 
        
        if author == None: 
            self.write(self.books.json_list())
        else : 
            result = self.books.get_books_from_author(author)
            
            if result == None:
                self.set_status(204)
            else :
                self.write(result)
           