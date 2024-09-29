#Dieser Code ist geignet um die signale eines joysticks auszuleasen um sie in einem anderen script zu nutzen.
from machine import Pin, ADC
import utime

x_achse=ADC(Pin(27)) #Der x-achse des Joysticks wird Pin 27 zugewiesen
y_achse=ADC(Pin(26)) #Der y-achse des Joysticks wird Pin 26 zugewiesen
knopf=Pin(1, Pin.IN, Pin.PULL_UP) #Wenn man den stick runterdrückt geht das signal an Pin 1

while True:
    x_wert = x_achse.read_u16()
    y_wert = y_achse.read_u16()
    knopf_wert = knopf.value()
    
    
    print("X Wert:", x_wert, "Y Wert:", y_wert, "Knopf Wert:", knopf_wert)
    
    
    utime.sleep(1)
