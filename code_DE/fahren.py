# Dieser Code beinhaltet einige grundlegende Befehle zum steuern der Motoren.
from motor import Motor, BiMotor
import utime

# Initialize motors 
motor_links= BiMotor(11) # Belegt die Pins 11 und 12 für den linken Motor.
motor_rechts= BiMotor(14) # Belegt die Pins 14 und 15 für den rechten Motor.

def geradeaus(s): # "s" diefiniert die Geschwindigkeit
 motor_links.setForward(True)
 motor_rechts.setForward(True)

 motor_links.setSpeed(s)#minimum:14
 motor_rechts.setSpeed(s)#minimum:14
 
def links(s): # "s" diefiniert die Geschwindigkeit
 motor_links.setForward(True)
 motor_rechts.setForward(False)

 motor_links.setSpeed(s)#minimum:14
 motor_rechts.setSpeed(s)#minimum:14
 
def rechts(s): # "s" diefiniert die Geschwindigkeit
 motor_links.setForward(False)
 motor_rechts.setForward(True)

 motor_links.setSpeed(s)#minimum:14
 motor_rechts.setSpeed(s)#minimum:14

def zurück(s): # "s" diefiniert die Geschwindigkeit
 motor_links.setForward(False)
 motor_rechts.setForward(False)

 motor_links.setSpeed(s)#minimum:14
 motor_rechts.setSpeed(s)#minimum:14

def anhalten():
 motor_links.setSpeed(0)
 motor_rechts.setSpeed(0)
 
def beschleunigung(s): # "s" diefiniert die angestrebte Geschwindigkeit
 motor_links.setForward(True)
 motor_rechts.setForward(True)
 for i in range(40,s,1):
     motor_links.setSpeed(i)#minimum:14
     motor_rechts.setSpeed(i)#minimum:14
     utime.sleep_ms(i+120)
     
def abbremsen(s,j): # "s" diefiniert die angestrebte Geschwindigkeit "j" diefiniert die aktuelle geschwindigkeit und muss Individuell angepasst werden.
    for i in range (j,s,1):
        motor_links.setSpeed(i)
        motor_rechts.setSpeed(i)
        utime.sleep_ms(80-i+200)
        if s <15:
          anhalten
          
        
#-------Code ab hier------------------------------------------------------------------------------------------

