import asyncio
import os
import re
import socket
from HttpRequest import HttpRequest
from RequestHandler import RequestHandler
from FileRequestHandler import FileRequestHandler

class WebServer(RequestHandler):
    def __init__(self, ip,port):
        self.running = False
        self.ip = ip
        self.port = port
        self.request_handler : ARRAY[RequestHandler] = []
        self.apis : ARRAY[API] = []
        
    def set_running(self,_running: bool):
        self.running = _running
        
    def add_api(self,api:API):
        print("Adding RequestHandlers for API '"+api.api_name+"'...")
        for handler in api.get_handlers():
            self.add_request_handler(handler)
    def add_www_file_request_handlers(self):
        #add FileRequestHandler for each file in /www/*
        print("Adding FileRequestHandlers for '/www/*'...")
        for fileName in os.listdir('www'):
            self.add_request_handler(FileRequestHandler('/'+str(fileName),'GET'))
            if fileName == 'index.html':
                self.add_request_handler(FileRequestHandler('/','GET'))
    
    def add_request_handler(self,requestHandler: RequestHandler):
        for rh in self.request_handler:
            if rh.type == requestHandler.type and rh.url == requestHandler.url:
                print('RequestHandler already defined:',requestHandler.to_string())
                return
        print('Adding RequestHandler:',requestHandler.to_string())
        self.request_handler += [requestHandler]

    async def request_callback(self,sr: asyncio.stream.StreamReader, sw: asyncio.StreamWriter):
        try:
            #parse to HttpRequest
            data = await sr.read(1024)
            request = HttpRequest(data.decode('UTF-8'))
            responseContent = await self.handle_request(request)
            #print("writing response:",responseContent)
            sw.write(responseContent)
            await asyncio.wait_for(sw.drain(),10)
            #print("handled callback",responseContent)
        finally:
            sw.close()
            await sw.wait_closed()
    async def handle_request(self,httpRequest: HttpRequest) -> str:
        
        for rh in self.request_handler:
            if rh.type == httpRequest.type and re.match("^"+rh.url+"$",httpRequest.url):
                print("New HttpRequest",str(rh.to_string()))
                if rh.api_context == None:
                    return await rh.handle_request(httpRequest)
                else:
                    return await rh.handle_request(rh.api_context,httpRequest)
        
        print("No RequestHandler found!",httpRequest.to_string())
        responseContent = 'HTTP/1.1 404 Not Found'
        return responseContent
