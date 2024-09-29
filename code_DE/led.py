import utime
from machine import Pin

#led=Pin("LED", Pin.OUT) # Für den Pico mit eingebautem WLAN
led=Pin(25, Pin.OUT) # Für den Pico ohne WLAN

def blinken():
 while True:
  led.value(1)
  utime.sleep(1)
  led.value(0)

def an():
 led.value(1)
 
def aus():
 led.value(0)