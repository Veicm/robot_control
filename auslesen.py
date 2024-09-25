from machine import Pin, ADC
import utime

xAxis=ADC(Pin(27))
yAxis=ADC(Pin(26))
button=Pin(1, Pin.IN, Pin.PULL_UP)

while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue = button.value()
    
    
    print("X Value:", xValue, "Y Value:", yValue, "Button Value:", buttonValue)
    
    
    utime.sleep(1)