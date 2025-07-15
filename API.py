from RequestHandler import RequestHandler

# Handler to manage the APIs
# controls a list of handlers, gathered by the @ApiPath-Declarotor
# handlers can be matched by the api_name
class API_Handler:
    def __init__(self):
        self.api_name = ""
        self.method_names = []
        self.handlers = []
        pass
    # api_name should be unique
    def set_api_name(self,_api_name):
        self.api_name = _api_name       
handler : API_Handler = API_Handler()

# @ApiPath Decorator to define a ApiPath-Function
def ApiPath(request_pattern,request_type = 'GET'):
    global handler
    def decorate_apiPath(func):
        print("New API-Mapping:  ["+str(request_type)+"]",str(request_pattern)+" -> '"+str(handler.api_name)+"."+str(func.__name__)+"()'")
        handler.method_names += [str(func.__name__)]
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            return result
        rh = RequestHandler(request_pattern, request_type)
        rh.api_name = handler.api_name
        rh.handle_request = wrapper
        handler.handlers += [rh]
        return wrapper
    return decorate_apiPath
    
# @Api Decorator to define a API-Object
# api_name should be unique
def Api(api_name = ""):
    global handler
    print("Defining New API: ["+str(api_name)+"]")
    handler.set_api_name(api_name)
    def decorate_api(func):
        def wrapper(*args, **kwargs):
            print("API created",api_name)
            result = func(*args, **kwargs)
            result.set_api_name(api_name)
            return result
        return wrapper
    return decorate_api
    
class API:
    def __init__(self):
        self.api_name = ""
    # called by the @Api decorator.
    # api_name should be unique
    def set_api_name(self,_api_name):
        self.api_name = _api_name
        
    # match handlers by api_name and set api_context
    def get_handlers(self):
        global handler
        handlers = []
        for h in handler.handlers:
            if h.api_name == self.api_name:
                h.api_context = self
                handlers += [h]
        return handlers
