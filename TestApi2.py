from API import API
from API import ApiPath
from API import Api

@Api("TestApi2")
class TestApi2(API):
    @ApiPath("/te.*","GET")
    async def test_path2(self,httpRequest: HttpRequest):
        print("Handling Request:",httpRequest.to_string())
        print("hello")
        return "hello test2"
    def test2(self):
        print("hello")

