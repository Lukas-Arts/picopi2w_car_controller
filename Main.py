import asyncio
from machine import Pin
from WiFi import WiFi
from WebServer import WebServer
from Controller import Controller
from TestApi import TestApi
class MAIN:
    def __init__(self):
        wifi_status_led = Pin("LED",Pin.OUT)
        wifi_status_led.off()
        wifi = WiFi(wifi_status_led, "SSID", "PW")
        ip = wifi.connect()
        self.server = WebServer(ip,80)
        
        #add request handlers
        self.controller = Controller()
        test = TestApi(self.controller)
        self.server.add_api(test)
        self.server.add_www_file_request_handlers()
        
        asyncio.run(self.start())
        
    async def start(self):
        #start serve loop
        distanceTask = asyncio.create_task(self.controller.get_distance())
        self.server.set_running(True)
        serveTask = await asyncio.start_server(self.server.request_callback,"0.0.0.0",80)
        
        while self.server.running:
            distanceTask = asyncio.create_task(self.controller.auto())
            await asyncio.sleep(0.5)
            #print(f"Both tasks have completed now: {serveTask}, {distanceTask.done()}")