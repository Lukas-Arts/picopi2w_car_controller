import json
from API import API
from API import API_Handler
from Controller import Controller


class TestApi(API):
    api = API.api
    api.set_api_name("TestApi")
    def __init__(self,_controller: Controller):
        super().__init__("TestApi")
        self.controller = _controller
        pass
    
    def test2(self):
        print("hello")
    
    @api.apiPath("/joyControl","POST")
    async def joystick(self,httpRequest: HttpRequest):
        print("Handling Joystick Request:",httpRequest.to_string())
        jsonContent = json.loads(httpRequest.content)
        await self.controller.joystick(jsonContent['x'],jsonContent['y'],jsonContent['speed'],jsonContent['angle'])
        return 'HTTP/1.1 200 OK'
        
    @api.apiPath("/","POST")
    async def joypad(self,httpRequest: HttpRequest):
        print("Handling Action Request:",httpRequest.to_string())
        if httpRequest.content == 'action=forward':
            self.controller.forward()
        elif httpRequest.content == 'action=backward':
            self.controller.backward()
        elif httpRequest.content == 'action=left':
            self.controller.left()
        elif httpRequest.content == 'action=center':
            self.controller.center()
        elif httpRequest.content == 'action=right':
            self.controller.right()
        elif httpRequest.content == 'action=toggle_state':
            self.controller.toggle_state()
        file = open('www/index.html')
        responseContent = file.read()
        #responseContent = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nContent-Length: ["+str(len(responseContent))+"]\r\n\r\n"+responseContent
        file.close()
        #update and return html 
        distance = await self.controller.get_distance()
        responseContent = responseContent.format(self.controller.state,str(distance))
        return responseContent
    
    # use custom instead of default FileRequestHandlers for index to write distance to html
    @api.apiPath("/")
    @api.apiPath("/index.html")
    async def index2(self,httpRequest: HttpRequest):
        print("Handling Request:",httpRequest.to_string())
        file = open('www/index.html')
        responseContent = file.read()
        #responseContent = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nContent-Length: ["+str(len(responseContent))+"]\r\n\r\n"+responseContent
        file.close()
        #update and return html
        distance = await self.controller.get_distance()
        responseContent = responseContent.format(self.controller.state,str(distance))
        return responseContent
