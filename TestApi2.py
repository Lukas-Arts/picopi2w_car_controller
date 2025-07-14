from API import API
from API import API_Handler
class TestApi2(API):
    api = API.api
    api.set_api_name("TestApi2")
    def __init__(self):
        super().__init__("TestApi2")
        pass
    @api.apiPath("/test2","GET")
    async def test_path2(self,httpRequest: HttpRequest):
        print("Handling Request:",httpRequest.to_string())
        print("hello")
        return "hello test2"
    def test2(self):
        print("hello")

