import utime
from machine import Pin


red=Pin(20,Pin.OUT)
blue=Pin(19,Pin.OUT)
green=Pin(21,Pin.OUT)

#grund definition

def rot_an():
    red.value(1)

def rot_aus():
    red.value(0)

def blau_an():
    blue.value(1)

def blau_aus():
    blue.value(0)

def grün_an():
    green.value(1)

def grün_aus():
    green.value(0)

def alle_an():
    rot_an()
    blau_an()
    grün_an()

def alle_aus():
    rot_aus()
    blau_aus()
    grün_aus()

#grund-befehl definition
def rot_only():
    alle_aus()
    rot_an()
    
def blau_only():
    alle_aus()
    blau_an()
    
def grün_only():
    alle_aus()
    grün_an()
    
def rot_blinken(s,d):
    while 0<d:
        d=d-1
        rot_an()
        utime.sleep(1/s)
        rot_aus()
        
def blau_blinken(s,d):
    while 0<d:
        d=d-1
        blau_an()
        utime.sleep(1/s)
        blau_aus()

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
        blau_only()
        utime.sleep(1/s)
        grün_only()
        utime.sleep(1/s)
        blau_an()
        utime.sleep(1/s)
        rot_an()
        utime.sleep(2/s)
        alle_aus()
        utime.sleep(3/s)

#----Code ab Hier------------------------------------------------------------------------------


disco(15,500)