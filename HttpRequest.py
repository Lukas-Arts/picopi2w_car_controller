
class HttpRequest:
    def __init__(self,_request_string):
        self.request = _request_string.splitlines()
        print(self.request[0])
        self.type = self.request[0].split()[0]
        if self.type != 'OPTIONS':
            self.url = self.request[0].split()[1]
        
        self.request_dict = {}
        isContent = False
        self.content = ""
        for i in range(len(self.request)):
            if i != 0:
                if isContent:
                    self.content+=self.request[i]
                elif self.request[i] == '':
                    isContent = True
                else:
                    arr = self.request[i].split()
                    self.request_dict[arr[0]] = self.request[i].replace(arr[0],'',1)
            
        print(self.type+' '+self.url)
        print(self.content)
