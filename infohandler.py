import tornado.web
import book
import json
import asyncio 

class InfoHandler(tornado.web.RequestHandler):
  
    async def get(self):
        message = """<html>
        <head></head>
        <body><h2>Info API</h2>
        """      
        message = message + "<hr><p> <b>http://localhost:8888/books</b> - \
                             Microservice Root </p><p>GET - Returns HTML</p>"
        message = message + "<hr><p> <b>http://localhost:8888/books/info</b> - \
                             Api Information Page (this page) </p><p>GET - Returns HTML</p>"
        message = message + "<hr><p> <b>http://localhost:8888/books/addbook?title=\"Book Title\"&author=\"Book Author\"</b>\
                             - Api to add a book. Does not accept duplicates </p><p>POST - Returns JSON</p>"
        message = message + "<hr><p> <b>http://localhost:8888/books/delbook?title=\"Book Title to delete\"</b>\
                             - Api to delete a book </p><p>DELETE - Returns simple text</p>"
        message = message + "<hr><p> <b>http://localhost:8888/books/listbooks</b> -\
                             Api to list all books </p><p>GET - Returns JSON</p>"
        message = message + "<hr><p> <b>http://localhost:8888/books/listbooks?author=\"Auhtor\"</b>\
                             - Api to list all books from author </p><p>GET - Returns JSON</p>"                 
        message = message + "<hr><p> <b>http://localhost:8888/books/bookdetails?title=\"Title\"</b>\
                             - Api to produce HTML for the book with title </p><p>GET Returns HTML page</p>"                         
        message = message + """</body> </html>"""   
        
        self.set_status(200)
        self.write(message)