import tornado.web

class ErrorHandler(tornado.web.RequestHandler):

    """Generates an error response with status_code for all requests. 
    NOTE: This is not correct! """
    

    def write_error(self, status_code, **kwargs):
        print ('In get_error_html. status_code: ', status_code)
        if status_code in [403, 404, 500, 503]:
            self.write('Error %s' % status_code)
        else:
            self.write('BOOM!')

    def prepare(self):
        print ('In prepare...')
        self.write('BOOM!')        
        # raise Exception('Error!')