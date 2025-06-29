from servo import Servo
class Controller:
    def __init__(self):
        self.servo1 = Servo(28,deg_range = 180)
        self.servo1.set_deg(90)
        self.servo2 = Servo(7,deg_range = 360)
        self.servo2.set_servo_speed(0)
        pass
    def forward(self):
        self.servo2.set_servo_speed(50)
        pass
    def backward(self):
        self.servo2.set_servo_speed(-50)
        pass
    def left(self):
        self.servo1.set_deg(0)
        pass
    def center(self):
        self.servo1.set_deg(90)
        self.servo2.set_servo_speed(0)
        pass
    def right(self):
        self.servo1.set_deg(180)
        pass