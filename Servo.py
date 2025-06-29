from machine import Pin,PWM
import time

class Servo:
    def __init__(self,pin_num,freq = 50,min_duty = 1638,max_duty = 8191,deg_range = 180):
        self.servo=PWM(Pin(pin_num))
        self.servo.freq(freq)
        self.min_duty=min_duty
        self.max_duty=max_duty
        self.deg_range=deg_range
    def set_deg(self,deg):
        self.servo.duty_u16(self.get_duty_from_deg(deg))
    def set_duty(self,duty):
        self.servo.duty_u16(duty)
    def get_duty(self):
        self.servo.duty_u16()
    def get_duty_from_deg(self,deg):
        duty = self.min_duty+int((deg*(self.max_duty-self.min_duty)/self.deg_range))
        return duty;
    def get_deg_from_duty(self,duty):
        deg = (duty-self.min_duty)/((self.max_duty-self.min_duty)/self.deg_range)
        return deg;

        
    # make sure the way is free, as this function repetedly tries moves the servo into the direction
    def move_deg_in_time(self,deg,time_to_move):
        min_movement_speed=5 # the servos movement speed in ms
        start_deg=self.get_deg_from_duty(self.servo.duty_u16())
        to_deg=start_deg+deg
        self.move_to_deg_in_time(to_deg,time_to_move)
        
    # make sure the way is free, as this function repetedly tries moves the servo into the direction
    def move_to_deg_in_time(self,to_deg,time_to_move):
        if(to_deg<0 or to_deg>self.deg_range):
            print("ERROR: trying to move out of range!!")
            return
        min_movement_speed=5 # the servos movement speed in ms
        start_duty=self.servo.duty_u16()
        end_duty=self.get_duty_from_deg(to_deg)
        duty_steps_total=end_duty-start_duty
        steps=time_to_move/min_movement_speed
        duty_steps=duty_steps_total/(steps)
        current=start_duty
        for i in range(0, steps+1):
            next_duty=int(start_duty+i*duty_steps)
            #print(next_duty)
            self.servo.duty_u16(next_duty)
            current=next_duty
            time.sleep_ms(min_movement_speed)
        print('start duty: '+str(start_duty)+' end duty: '+str(end_duty)+' steps '+str(steps)+' step '+str(duty_steps))
    
    #for use with 360° servos
    def set_servo_speed(self,percent):
        percent = percent - 3
        """
        Steuerung des 360°-Servos.
        -100 = volle Geschwindigkeit rückwärts
         0   = Stillstand
        +100 = volle Geschwindigkeit vorwärts
        """
        percent = max(-100, min(100, percent))  # Clamp auf -100...100

        # Mappe -100..0..+100 auf 2.5%..7.5%..12.5%
        duty_percent = 7.5 + (percent / 100) * 5  # 5 % = Abstand zur Mitte

        duty_u16 = int((duty_percent / 100) * 65535)
        self.servo.duty_u16(duty_u16)

