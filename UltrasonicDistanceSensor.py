from machine import Pin
from time import sleep, sleep_us, ticks_us

class UltrasonicDistanceSensor:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger = Pin(trigger_pin,Pin.OUT)
        self.echo = Pin(echo_pin,Pin.IN)
        
        self.last_read_tick = ticks_us()
        self.last_read = 0
    def get_spee_of_sound_from_temp(self,temp_in_deg):
        # speed of sound at 20° + (estimated 0.000059 per deg) *diff
        speed_of_sound=0.034346+(temp_in_deg-20)*0.0000585
        print('    spee of sound:', speed_of_sound)
        return speed_of_sound
    
    def get_distance(self,temp_in_deg):
        current_read_tick = ticks_us()
        # more than 0.5s passed
        diff = current_read_tick - self.last_read_tick
        if (diff) > 500000:
            print('read diff: ', str((current_read_tick - self.last_read_tick)))
            self.last_read_tick = current_read_tick
            # Abstand messen 
            self.trigger.low()
            sleep_us(2)
            self.trigger.high()
            sleep_us(10)
            self.trigger.low()
            # Zeitmessungen
            while self.echo.value() == 0:
               signaloff = ticks_us()
            while self.echo.value() == 1:         
               signalon = ticks_us()
            # Vergangene Zeit ermitteln
            timepassed = signalon - signaloff
            # Abstand/Entfernung ermitteln
            # Entfernung über die Schallgeschwindigkeit (34320 cm/s bei 20 °C) berechnen
            # Durch 2 teilen, wegen Hin- und Rückweg
            abstand = timepassed * self.get_spee_of_sound_from_temp(temp_in_deg) / 2
            print('    Off:', signaloff)
            print('     On:', signalon)
            print('   Zeit:', timepassed)
            print('Abstand:', str("%.2f" % abstand), 'cm')
            self.last_read = abstand
        else:
            print('Lezter Abstand:', str("%.2f" % self.last_read), 'cm ',diff)
        
        return self.last_read
