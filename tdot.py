from motor import Motor, BiMotor
from ultrasonic import Ultra
# Initialize motors
s = 50
motor_left= BiMotor(11) # Initializing pins 11 and 12 for left motor.
motor_right= BiMotor(14) # Initializing pins 14 and 15 for right motor.
ultra = Ultra(16)
motor_left.setForward(False)
motor_right.setForward(False)


while ultra.getDist() >10:
    motor_left.setSpeed(s)#minimum:14
    motor_right.setSpeed(s)
    
motor_left.setSpeed(0)
motor_right.setSpeed(0)
