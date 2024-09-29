# import motor
from motor import Motor, BiMotor
import utime

# Initialize motors 
motor_left= BiMotor(11) # Initializing pins 11 and 12 for left motor.
motor_right= BiMotor(14) # Initializing pins 14 and 15 for right motor.

def geradeaus(s):
 motor_left.setForward(True)
 motor_right.setForward(True)

 motor_left.setSpeed(s)#minimum:14
 motor_right.setSpeed(s)#minimum:14
 
def links(s):
 motor_left.setForward(True)
 motor_right.setForward(False)

 motor_left.setSpeed(s)#minimum:14
 motor_right.setSpeed(s)#minimum:14
 
def rechts(s):
 motor_left.setForward(False)
 motor_right.setForward(True)

 motor_left.setSpeed(s)#minimum:14
 motor_right.setSpeed(s)#minimum:14

def zurück(s):
 motor_left.setForward(False)
 motor_right.setForward(False)

 motor_left.setSpeed(s)#minimum:14
 motor_right.setSpeed(s)#minimum:14
 
def beschleunigung(s):
 motor_left.setForward(True)
 motor_right.setForward(True)
 for i in range(40,s,1):
     motor_left.setSpeed(i)#minimum:14
     motor_right.setSpeed(i)#minimum:14
     utime.sleep_ms(i+120)
     
def abbremsen(s,j):
    for i in range (j,s,1):
        motor_left.setSpeed(i)
        motor_right.setSpeed(i)
        utime.sleep_ms(80-i+200)
        

geradeaus(100)
#bei neuer batterie WECHELN
