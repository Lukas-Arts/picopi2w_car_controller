from Servo import Servo
from UltrasonicDistanceSensor import UltrasonicDistanceSensor
class Controller:
    def __init__(self):
        self.servo1 = Servo(28,deg_range = 180)
        self.servo1.set_deg(90)
        self.servo2 = Servo(7,deg_range = 360)
        self.servo2.set_servo_speed(0)
        self.distanceSensor = UltrasonicDistanceSensor(17,16)
        pass
    def forward(self):
        self.servo2.set_servo_speed(50)
        pass
    def backward(self):
        self.servo2.set_servo_speed(-50)
        pass
    def left(self):
        self.servo1.set_deg(70)
        pass
    def center(self):
        self.servo1.set_deg(90)
        self.servo2.set_servo_speed(0)
        pass
    def right(self):
        self.servo1.set_deg(110)
        pass
    def get_distance(self):
        return self.distanceSensor.get_distance(20)
    
    # x/y - coordinates, +-
    # speed - distance from center, 0-100
    # angle - 0-360, 90 front, 0 right, 270 bottom,  180 left
    #
    def joystick(self,x,y,speed,angle):
        distance = self.distanceSensor.get_distance(20)
        print(distance)
        if distance > 10.0:
            print(str(speed)+" "+str(angle))
            speed2 = y/(-4) # speed based on y
            self.servo2.set_servo_speed(speed2)
            self.servo1.set_deg(90+(x/10))
        else:
            self.servo2.set_servo_speed(0)
        pass
