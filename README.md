# PicoPI 2 W Car Controller

Starts a WebServer on the PI that connects to the predefined WiFi to display UI (JoyStick, JoyPad, Buttons, Values) to control a PI-based Lego-Car.

##Hardware needed:
- PicoPI W or Pico PI 2 W
- Servos, I used Lego-compatible ones from M5Stack
- HC-SR04 - Ultrasonic Sensor (be aware of 5V vs 3.3V versions and the need of a voltage divider for the ECHO-Pin in case of the 5V version)

##Setup

Set your wifi SSID and PW in the Main.py. Rename the Main.py if autostart is needed (with a power bank, for wireless interaction)
'''
        wifi = WiFi(wifi_status_led, "SSID", "PW")
'''

Connect your servos and sensors according to the setup in Controller.py or adjust it there
'''
        self.servo1 = Servo(28,deg_range = 180)
        self.servo1.set_deg(90)
        self.servo2 = Servo(7,deg_range = 360)
        self.servo2.set_servo_speed(0)
        self.distanceSensor = UltrasonicDistanceSensor(17,16)
'''

##Play

Use a battery or powerbank and setup autostart to control the car wireless.
The PicoPI logs its IP to the console when its connected, otherwise look it up in you router/AP.
Open the controls on ./, ./index.html or ./joy.html and control the car.