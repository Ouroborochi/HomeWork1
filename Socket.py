import os 
import socket 

_socket = socket.socket() 
_socket.bind(('localhost',8000)) 
_socket.listen(1) 

while True: 
    connection, address = _socket.accept() 
    data = connection.recv(1024) 
    request=data.decode('utf-8') 
    print(request) 
    address = request[1][1:]
    if (address=="/"):
        address="/index.html"
    if(os.path.exists(address)):
        file=open(address,mode='r')
        request="""HTTP/1.1 200 OK \n Content type:text HTML\n\n\n """ + file.read()
        print (request)
        connection.send(request.encode('utf-8'))
        file.close() 
    connection.close() 
_socket.close()