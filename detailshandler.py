import tornado.web
import book
import json
import asyncio 
import base64

class DetailsHandler(tornado.web.RequestHandler):
    def initialize(self, books):
        self.books = books
        
    async def get(self):
        
        result="[]"
        
        title = self.get_argument("title", None) 
        
        if title == None: 
            self.set_status(404)
        else : 
            result = self.books.get_book_with_title(title)
            
            if result == None:
                self.set_status(204)
            else :
                data_uri = base64.b64encode(open('book.png', 'rb').read()).decode('utf-8')
                img_tag = '<hr><p><center><img src="data:image/png;base64,{0}"></center></p>'.format(data_uri)                
                
                # Only 1 item in list 
                mybook = result[0] 
                # Takes the book and returns HTML Code 
                htmlbook = """<html>
                <head></head>
                <body><h2>Book Details :</h2>
                """      
                htmlbook = htmlbook + img_tag 
                htmlbook = htmlbook + "<hr><p> <b>Title: </b> " + mybook['Title'] + " </p>"    
                htmlbook = htmlbook + "<hr><p> <b>Author: </b> " + mybook['Author'] + " </p>"            
                
                htmlbook = htmlbook + """<hr></body> </html>"""   
                
                self.set_status(200)
                self.write(htmlbook)                