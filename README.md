# PicoPI 2 W Car Controller

Starts a WebServer on the PI that connects to the predefined WiFi to display UI (JoyStick, JoyPad, Buttons, Values) to control a PI-based Lego-Car.

## Hardware needed

- PicoPI W or Pico PI 2 W
- Servos, I used Lego-compatible ones from M5Stack
- HC-SR04 - Ultrasonic Sensor (be aware of 5V vs 3.3V versions and the need of a voltage divider for the ECHO-Pin in case of the 5V version)
- Lego or othe base material
- (battery for full wireless experience)

## Setup

#### WiFi

Set your wifi SSID and PW in the Main.py. Rename the Main.py if autostart is needed (with a power bank, for wireless interaction)

```
        wifi = WiFi(wifi_status_led, "SSID", "PW")
```

#### Control

Connect your servos and sensors according to the setup in Controller.py or adjust it there

```
        self.servo1 = Servo(28,deg_range = 180)
        self.servo1.set_deg(90)
        self.servo2 = Servo(7,deg_range = 360)
        self.servo2.set_servo_speed(0)
        self.distanceSensor = UltrasonicDistanceSensor(17,16)
```

Edit the Control.auto()-function to use the sensors for autonoumous-drive-mode
```
    async def auto(self):
        await self.get_distance()
        if self.state == 'auto':
            # drive autonomously using the sensors
            pass
```

#### Webserver 

You can either add an RequestHandler directly with WebServer.add_request_handler() or define a
API by inheriting from API and setting a static API_Handler in the init.

```
from API import API
from API import API_Handler
class TestApi2(API):
    api = API_Handler("TestApi2")
    def __init__(self):
        self.api_handler = self.api
        pass
```

Then use the @api.apiPath(path_patter,request_type='GET')-decorator to annotate your API-Path-Function

```
    @api.apiPath("/test2","GET")
    def test_path2(self,httpRequest: HttpRequest):
        print("Handling Request:",httpRequest.to_string())
        print("hello")
```

and finally add your API to the WebServer in the Main

```
        test = TestApi2()
        self.server.add_api(test)
```

## Play

Use a battery or powerbank and setup autostart to control the car wireless.
The PicoPI logs its IP to the console when its connected, otherwise look it up in you router/AP.
Open the controls on http://%IP%/, http://%IP%/index.html or http://%IP%/joy.html in your browser and control the car from your phone on the go.
