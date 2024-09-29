from machine import *
import utime
irm=Pin(21,Pin.IN,Pin.PULL_UP)
irl=Pin(26,Pin.IN,Pin.PULL_UP)
irr=Pin(27,Pin.IN,Pin.PULL_UP)

while True:
    print(irr.value())
    while irr.value() == 0:
        utime.sleep_ms(50)
    print(irr.value())
    while irr.value() == 1:
        utime.sleep_ms(50)
        
#Ausgabe "0", wenn Hindernis erkannt wird, "1" wenn kein Hindernis erkannt wird. Im Sonnenschein funktioniert der Sensor nicht gut.