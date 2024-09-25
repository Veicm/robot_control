from machine import Pin
from time import sleep
import utime

class Ultra:
   def __init__(self, pinNo):
       self.trigger = Pin(pinNo, Pin.OUT) # to trigger a sound impulse
       self.echo = Pin(pinNo+1, Pin.IN) # records the echo of the trigger pulse      

   def getDist(self):
       timepassed = 0
       signalon = 0
       signaloff = 0
       self.trigger.low()
       utime.sleep_us(2)
       self.trigger.high()
       utime.sleep_us(5)
       self.trigger.low()
       while self.echo.value() == 0:
           signaloff = utime.ticks_us()
       while self.echo.value() == 1:
           signalon = utime.ticks_us()
       timepassed = signalon - signaloff
       distance = round((timepassed * 0.0343) / 2, 2)
       print("The distance from object is ", distance, "cm.")
       utime.sleep_ms(100) # Wait necessary or program halts
       return distance