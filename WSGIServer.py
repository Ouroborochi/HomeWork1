import os
from wsgiref.simple_server import make_server

top = "<div class='top'>Middleware TOP</div>"
bottom =  "<div class='botton'>Middleware BOTTOM</div>"

class MiddleWare(object):
    def __init__(self, app):
        self.app = app
        
    def __call__(self, environ, start_response):
        page = self.app(environ, start_response)[0]
        if (page.find('<body>') > 0):
            header,body = page.split('<body>')
            data,htmlend = body.split('</body>')
            data = '<body>'+ top + data + bottom+'</body>'
            value = header + data + htmlend
            return value
        else:
            value = top + page + bottom
            return value

def app(environ, start_response):   
    path = environ['PATH_INFO']
    filePath = '.' + path  
    if not os.path.isfile(filePath):
        filePath ='./index.html' 
    file = open(filePath,'r')
    fileContent = file.read()
    file.close()
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [fileContent]

app = MiddleWare(app)

if __name__=='__main__':
    server=make_server("localhost",8080,MiddleWare(app))
    print ("Serving localhost on port 8080...")
    server.serve_forever()