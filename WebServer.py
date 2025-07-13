import os
import json
import socket
from HttpRequest import HttpRequest
class WebServer:
    def __init__(self, ip,port,controller):
        self.running = False
        self.ip = ip
        self.port = port
        self.controller = controller
        print("Starting WebServer on "+ip+":"+str(port)+"...")
        
        self.conntection = self.open_socket(self.ip,self.port)
        print("Socket opened...")
        self.serve(self.conntection)
    def set_running(self,_running):
        self.running = _running

    def open_socket(self,ip,port):
        # Open a socket
        address = (ip, port)
        next_socket = socket.socket()
        # reuse old socket if available
        next_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        # bind socket
        next_socket.bind(address)
        next_socket.listen(1)
        return next_socket

    def serve(self,next_socket):
        self.running = True
        #listen for new requests
        try:
            while self.running:
                #accept connection
                connection = next_socket.accept()[0]
                try:
                    #parse to HttpRequest
                    request = HttpRequest(connection.recv(1024).decode('UTF-8'))
                    
                    #read content from file, if available
                    urlWithoutFirstSlash = request.url.replace('/','',1)
                    if request.url == '/':
                        urlWithoutFirstSlash = 'index.html'
                    responseContent = ""
                    for fileName in os.listdir('www'):
                        print(fileName)
                        if fileName == urlWithoutFirstSlash:
                            file = open('www/'+fileName)
                            responseContent = file.read()
                            file.close()
                            if fileName == 'index.html':
                                #update and return html
                                distance = self.controller.get_distance()
                                responseContent = responseContent.format("adsf",str(distance))
                            
                    # or use controller to handle requests
                    if request.url == '/':
                        if request.content == 'action=forward':
                            self.controller.forward()
                        elif request.content == 'action=backward':
                            self.controller.backward()
                        elif request.content == 'action=left':
                            self.controller.left()
                        elif request.content == 'action=center':
                            self.controller.center()
                        elif request.content == 'action=right':
                            self.controller.right()
                        elif responseContent == '':
                            responseContent = 'HTTP/1.1 404 Not Found'
                    elif request.url == '/joyControl':
                        jsonContent = json.loads(request.content)
                        self.controller.joystick(jsonContent['x'],jsonContent['y'],jsonContent['speed'],jsonContent['angle'])
                        responseContent = 'HTTP/1.1 200 OK'
                    elif responseContent == '':
                        responseContent = 'HTTP/1.1 404 Not Found'
                    
                    #print(responseContent)
                    connection.send(responseContent)
                finally:
                    connection.close()
        finally:
            next_socket.close()
