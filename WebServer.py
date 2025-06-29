import socket
class WebServer:
    def __init__(self, ip,port,controller):
        self.ip = ip
        self.port = port
        self.controller = controller
        print("Starting WebServer on "+ip+":"+str(port)+"...")
        
        self.conntection = self.open_socket(self.ip,self.port)
        print("Socket opened...")
        self.serve(self.conntection)

    def open_socket(self,ip,port):
        # Open a socket
        address = (ip, port)
        connection = socket.socket()
        connection.bind(address)
        connection.listen(1)
        return connection

    def serve(self,connection):
        #listen for new requests
        while True:
            client = connection.accept()[0]
            request = client.recv(1024)
            request = str(request)
            try:
                request = request.split()[1]
            except IndexError:
                pass
            if request == '/forward?':
                self.controller.forward()
            elif request =='/backward?':
                self.controller.backward()
            elif request == '/left?':
                self.controller.left()
            elif request == '/center?':
                self.controller.center()
            elif request == '/right?':
                self.controller.right()
            html = self.webpage("")
            client.send(html)
            client.close()

    def webpage(self,state):
        #Template HTML
        body = f"""
                <div class="container">
                    <div>
                    </div>
                    <div>
                        <form action="./forward">
                        <input type="submit" value="&#11205;" />
                        </form>
                    </div>
                    <div>
                    </div>
                    <div>
                        <form action="./left">
                        <input type="submit" value="&#11207;" />
                        </form>
                    </div>
                    <div>
                        <form action="./center">
                        <input type="submit" value="&#9208;" />
                        </form>
                    </div>
                    <div>
                        <form action="./right">
                        <input type="submit" value="&#11208;" />
                        </form>
                    </div>
                    <div>
                    </div>
                    <div>
                        <form action="./backward">
                        <input type="submit" value="&#11206;" />
                        </form>
                    </div>
                    <div>
                    </div>
                </div>
                <p>State is {state}</p>
                """
        html = """
                <!DOCTYPE html>
                <html>
                <head>
                <style>
                .container {
                  display: grid;
                  grid-template-columns: auto auto auto;
                }
                .container > div {
                  background-color: #f1f1f1;
                  font-size: 30px;
                  text-align: center;
                }
                </style>
                <meta charset="UTF-8">
                </head>
                <body>
                """+body+"""
                </body>
                </html>
                """
        print(html)
        return str(html)
