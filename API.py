from RequestHandler import RequestHandler

    

class API_Handler:
    def __init__(self,_api_name):
        print("Handler created",_api_name)
        self.api_name = _api_name
        self.method_names = []
        self.handlers = []
        pass
    def set_api_name(self,_api_name):
        self.api_name = _api_name
    def apiPath(self,request_pattern,request_type = 'GET'):
        print("apipath called",request_pattern)
        #print(self)
        def decorator_apiPath(func):
            #print("decorator_apiPath called")
            print("API-Mapping: ["+str(request_type)+"]",str(request_pattern)+" -> '"+str(self.api_name)+"."+str(func.__name__)+"()'")
            self.method_names += [str(func.__name__)]
            def wrapper(self, *args, **kwargs):
                result = func(self, *args, **kwargs)
                return result
            rh = RequestHandler(request_pattern, request_type)
            rh.api_name = self.api_name
            rh.handle_request = wrapper
            print("new Handler",rh.to_string())
            self.handlers += [rh]
            return wrapper
        return decorator_apiPath
    
    
class API:
    api : API_Handler = API_Handler("")
    def __init__(self,_api_name):
        print("API created",_api_name)
        self.api_name = _api_name
        
    def get_handlers(self):
        handlers = []
        for handler in self.api.handlers:
            if handler.api_name == self.api_name:
                #print("found handler for API:",self.api_name,handler.to_string())
                handler.api_context = self
                handlers += [handler]
        return handlers
