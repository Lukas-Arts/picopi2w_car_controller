import json
from API import API
from API import ApiPath
from API import Api
from Controller import Controller

@Api("TestApi")
class TestApi(API):
    def __init__(self,_controller: Controller):
        self.controller = _controller
        pass
    
    def test2(self):
        print("hello")
    
    @ApiPath("/joyControl","POST")
    async def joystick(self,httpRequest: HttpRequest):
        print("Handling Joystick Request:",httpRequest.to_string())
        jsonContent = json.loads(httpRequest.content)
        await self.controller.joystick(jsonContent['x'],jsonContent['y'],jsonContent['speed'],jsonContent['angle'])
        return 'HTTP/1.1 200 OK'
        
    @ApiPath("/","POST")
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
        file.close()
        #update and return html 
        distance = await self.controller.get_distance()
        responseContent = responseContent.format(self.controller.state,str(distance))
        return responseContent
    
    # use custom instead of default FileRequestHandlers for index to write distance to html
    @ApiPath("/")
    @ApiPath("/index.html")
    async def index2(self,httpRequest: HttpRequest):
        print("Handling Request:",httpRequest.to_string())
        file = open('www/index.html')
        responseContent = file.read()
        file.close()
        #update and return html
        distance = await self.controller.get_distance()
        responseContent = responseContent.format(self.controller.state,str(distance))
        return responseContent
