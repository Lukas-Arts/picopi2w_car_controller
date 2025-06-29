from machine import Pin
from WiFi import WiFi
from WebServer import WebServer
from Controller import Controller

class MAIN:
    def __init__(self):
        wifi_status_led = Pin("LED",Pin.OUT)
        wifi_status_led.off()
        wifi = WiFi(wifi_status_led, "SSID", "PW")
        ip = wifi.connect()
        server = WebServer(ip,80,Controller())
    
