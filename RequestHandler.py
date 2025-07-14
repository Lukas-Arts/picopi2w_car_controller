from HttpRequest import HttpRequest

class RequestHandler:
    def __init__(self,_url: str,_type: str):
        self.url = _url
        self.type = _type
        self.api_context = None
    
    async def handle_request(self,httpRequest: HttpRequest) -> str:
        print("Handling Request:",httpRequest.to_string())
        pass
    def to_string(self) -> str:
        return "["+self.type+"] "+self.url