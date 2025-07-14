from RequestHandler import RequestHandler

class API:
    api_handler : API_Handler
    

class API_Handler:
    def __init__(self,_api_name):
        self.api_name = _api_name
        self.method_names = []
        self.handlers = []
        pass

    def apiPath(self,request_pattern,request_type = 'GET'):
        #print("apipath called")
        #print(self)
        def decorator_apiPath(func):
            #print("decorator_apiPath called")
            print("API-Mapping: ["+str(request_type)+"]",str(request_pattern)+" -> '"+str(self.api_name)+"."+str(func.__name__)+"()'")
            self.method_names += [str(func.__name__)]
            def wrapper(self, *args, **kwargs):
                result = func(self, *args, **kwargs)
                return result
            rh = RequestHandler(request_pattern, request_type)
            rh.handle_request = wrapper
            self.handlers += [rh]
            return wrapper
        return decorator_apiPath