# Dieses Programm läst den Roboter Fahren bis ein Hindernes kommt dann dreht er sich und fährt weiter.
# import motor
import utime
from machine import Pin
from motor import Motor, BiMotor
from ultrasonic import Ultra
from machine import *
# inizialisire Motor
motor_left= BiMotor(11) # Initializing pins 11 and 12 for left motor.
motor_right= BiMotor(14) # Initializing pins 14 and 15 for right motor.

#import led
#led=Pin("LED", Pin.OUT) # Für den Pico mit eingebautem WLAN
led=Pin(25, Pin.OUT) # Für den Pico ohne WLAN

#import Ampel
red=Pin(18,Pin.OUT)
yellow=Pin(19,Pin.OUT)
green=Pin(20,Pin.OUT)

#import Ultraschall
ultra = Ultra(16)

#import Infrarot
ir=Pin(21,Pin.IN,Pin.PULL_UP)


#motor shortcut bibliothek
def beschleunigung(s):
 motor_left.setForward(True)
 motor_right.setForward(True)
 for i in range(40,s,1):
     motor_left.setSpeed(i)#minimum:14
     motor_right.setSpeed(i)#minimum:14
     utime.sleep_ms(80-i+200)

def geradeaus(s):
 motor_left.setForward(True)
 motor_right.setForward(True)
 motor_left.setSpeed(s)#minimum:14
 motor_right.setSpeed(s)#minimum:14
 
def links(s):
 motor_left.setForward(False)
 motor_right.setForward(True)

 motor_left.setSpeed(s)#minimum:14
 motor_right.setSpeed(s)#minimum:14
 
def rechts(s):
 motor_left.setForward(True)
 motor_right.setForward(False)

 motor_left.setSpeed(s)#minimum:14
 motor_right.setSpeed(s)#minimum:14

def zurück(s):
 motor_left.setForward(False)
 motor_right.setForward(False)

 motor_left.setSpeed(s)#minimum:14
 motor_right.setSpeed(s)#minimum:14
 
def anhalten():
 motor_left.setForward(True)
 motor_right.setForward(True)

 motor_left.setSpeed(0)#minimum:14
 motor_right.setSpeed(0)#minimum:14
 
def erwiternder_radius():  #nur im ir zu benutzen
    f=0.5
    z=0.25
    if x%2==0:
        links(80)
        utime.sleep(z)
        utime.sleep(f)
        anhalten()
    else:
        rechts(80)
        utime.sleep(z)
        utime.sleep(f)
        
    
 

#Led Shortcut Bibliothek
def blinken():
 while True:
  led.value(1)
  utime.sleep(1)
  led.value(0)

def an():
 led.value(1)
 
def aus():
 led.value(0)
 
 
 
#ultraschall stopp 
def close(d):
  while ultra.getDist() > d:
   pass
  anhalten()
 
def tcasl(d):
  links(70)
  while ultra.getDist()<20:
      pass
  #utime.sleep_ms(500)
  anhalten()
 
def tcasr(d):
  rechts(70)
  while ultra.getDist()<20:
      pass
  #utime.sleep_ms(500)
  anhalten()
  
#Ampel
#für eine genauere Beschreibung öffne Ampel.py oder den Wiki eintrag zu diesem Script
  
#grund definition

def rot_an():
    red.value(1)

def rot_aus():
    red.value(0)

def gelb_an():
    yellow.value(1)

def gelb_aus():
    yellow.value(0)

def grün_an():
    green.value(1)

def grün_aus():
    green.value(0)

def alle_an():
    rot_an()
    gelb_an()
    grün_an()

def alle_aus():
    rot_aus()
    gelb_aus()
    grün_aus()

#grund-befehl definition
def rot_only():
    alle_aus()
    rot_an()
    
def gelb_only():
    alle_aus()
    gelb_an()
    
def grün_only():
    alle_aus()
    grün_an()
    
def rot_blinken(s,d):
    while 0<d:
        d=d-1
        rot_an()
        utime.sleep(1/s)
        rot_aus()
        
def gelb_blinken(s,d):
    while 0<d:
        d=d-1
        gelb_an()
        utime.sleep(1/s)
        gelb_aus()

def grün_blinken(s,d):
    while 0<d:
        d=d-1
        grün_an()
        utime.sleep(1/s)
        grün_aus()

def alle_blinken(s,d):
    while 0<d:
        d=d-1
        alle_an()
        utime.sleep(1/s)
        alle_aus()
    
#Komplex Befehl difinition

def disco(s,d):
    while 0<d:
        d=d-1
        alle_an()
        utime.sleep(2/s)
        rot_only()
        utime.sleep(1/s)
        gelb_only()
        utime.sleep(1/s)
        grün_only()
        utime.sleep(1/s)
        gelb_an()
        utime.sleep(1/s)
        rot_an()
        utime.sleep(2/s)
        alle_aus()
        utime.sleep(3/s)
        
        
        
        
#Ifrarot befehl
        
def test():
    while True:
        print(ir.value())
        while ir.value() == 0:
            utime.sleep_ms(50)
        print(ir.value())
        while ir.value() == 1:
            utime.sleep_ms(50)
        

def linie_folgen():
    x=1
    while True:
        f=0.5
        z=0.25
        print(ir.value())
        while ir.value() == 0:
            geradeaus(80)
            utime.sleep_ms(50)
        print(ir.value())
        while ir.value() == 1:
            if x%2==0:
                links(80)
                utime.sleep(z)
                utime.sleep(f)
                anhalten()
            else:
                rechts(80)
                utime.sleep(z)
                utime.sleep(f)
                anhalten()
            x=x+1
            f=f+0.5
            z=z+0.5

    

def main(geschwindigkeit)
    utime.sleep(2)
    x=0
    beschleunigung(geschwindigkeit)
    try:
        while True:
            u=ultra.getDist()
            while u<20:
                u=ultra.getDist()
                
                if x%2 ==0 :
                    an()
                    tcasr(20)
                    u=ultra.getDist()
                else:
                    an()
                    tcasl(20)
                    u=ultra.getDist()
                
                utime.sleep(0.3)
                aus()
                geradeaus(geschwindigkeit)
                x=x+1
    except KeyboardInterrupt:
        anhalten()
        print("Das Programm wurde beendet.")

# code ab hier -----------------------------------------
main(80)