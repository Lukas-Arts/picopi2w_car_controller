class HttpRequest:
    def __init__(self,_request_string: str):
        #print(self.headers[0])
        self.type = ""
        self.url = ""
        self.urlParameters = []
        self.urlWithoutParameters = ""
        self.content = ""
        self.request_dict = {}
        self.headers = _request_string.splitlines()
        isContent = False
        for i in range(len(self.headers)):
            if i == 0:
                self.type = self.headers[0].split()[0]
                if self.type != 'OPTIONS':
                    self.url = self.headers[0].split()[1]
                    urlParts = self.url.replace('/','',1).split('?')
                    self.urlWithoutParameters = urlParts[0]
                    if len(urlParts)>1:
                        self.urlParameters = urlParts[1].split("&")
                
            else:
                if isContent:
                    self.content+=self.headers[i]
                elif self.headers[i] == '':
                    isContent = True
                else:
                    arr = self.headers[i].split()
                    self.request_dict[arr[0]] = self.headers[i].replace(arr[0],'',1)
            
        #print(self.type+' '+self.url)
        #print(self.content)

    def to_string(self):
        s = "["+self.type+"] "+self.url
        if self.type == 'POST':
            s += " "+self.content
        return s
