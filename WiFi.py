import time
import machine
import network
import urequests

class WiFi:
    def __init__(self, status_led, ssid, pw):
        self.status_led = status_led
        self.status_led.value(False)
        self.ssid = ssid
        self.password = pw
        self.wlan = network.WLAN(network.STA_IF)
        if self.wlan.active():
            print('wifi was active before..')
            self.wlan.active(False)
            time.sleep(1)
        self.wlan.active(True)
    def is_connected(self):
        return self.wlan.status() == 3
    def shutdown(self):
        print('shutdown wifi..')
        self.wlan.disconnect()
        self.status_led.value(False)
    def connect(self):    
        self.wlan.connect(self.ssid, self.password)

        # Wait for connect or fail
        max_wait = 20
        while max_wait > 0:
            status = self.wlan.status()
            if status < -1 or status >= 3:
                break
            print('waiting for connection...'+str(status))
            if status == -1:
                self.wlan.connect(self.ssid, self.password)
            max_wait -= 1
            time.sleep(1)
        # Handle connection error
        if self.wlan.status() != 3:
            self.status_led.value(False)
            print(self.wlan.status())
            print(self.wlan.isconnected())
            raise RuntimeError('network connection failed')
        else:
            print('connected')
            self.status_led.value(True)
            status = self.wlan.ifconfig()
            print( 'ip = ' + status[0] )
            return status[0]
    def test(self):
        r = urequests.get("http://www.google.com")
        print(r.content)
        print(r.status_code)
        #r.json()

        r.close()
