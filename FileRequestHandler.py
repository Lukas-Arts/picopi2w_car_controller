from RequestHandler import RequestHandler

class FileRequestHandler(RequestHandler):
    def __init__(self,_url: str,_type: str):
        super().__init__(_url,'GET')
        if _url.startswith('..'):
            raise Exception('invalid url path')
    async def handle_request(self,httpRequest: HttpRequest) -> str:
        super().handle_request(httpRequest)
        u = self.url.replace('/','',1)
        if u == "":
            u = "index.html"
        file = open('www/'+u)
        responseContent = file.read()
        file.close()
        return responseContent
