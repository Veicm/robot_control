#Mit diesem Code wird die Ampel gesteuert es sind auch einige Funktionen vor definiert
import utime
from machine import Pin


rotes_licht=Pin(20,Pin.OUT) #für die rote Led wird Pin 20 definiert
gelbes_licht=Pin(19,Pin.OUT) #für die gelbe Led wird Pin 19 definiert
grünes_licht=Pin(21,Pin.OUT) #für die grüne Led wird Pin 21 definiert
#Bite überprüfe ob die angegeben Pins zu deiner Schaltung passen und ändere sie ggf.

#grund definition

def rot_an():
    rotes_licht.value(1) #die rote Led wird eingeschaltet

def rot_aus():
    rotes_licht.value(0) #die rote Led wird ausgeschaltet

def gelb_an():
    gelbes_licht.value(1) #die gelbe Led wird eingeschaltet

def gelb_aus():
    gelbes_licht.value(0) #die gelbe Led wird ausgeschaltet

def grün_an():
    grünes_licht.value(1) #die grüne Led wird eingeschaltet

def grün_aus():
    grünes_licht.value(0) #die grüne Led wird ausgeschaltet

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
    
def rot_blinken(s,d): #Die rote Led wird auf auf blinken gestellt (s gibt die geschwindigkeint an, d gibt die wiederholungen an)
    while 0<d:
        d=d-1
        rot_an()
        utime.sleep(1/s)
        rot_aus()
        
def gelb_blinken(s,d): #Die gelbe Led wird auf blinken gestellt (s gibt die geschwindigkeint an, d gibt die wiederholungen an)
    while 0<d:
        d=d-1
        gelb_an()
        utime.sleep(1/s)
        gelb_aus()

def grün_blinken(s,d): #Die grüne Led wird auf blinken gestellt (s gibt die geschwindigkeint an, d gibt die wiederholungen an)
    while 0<d:
        d=d-1
        grün_an()
        utime.sleep(1/s)
        grün_aus()

def alle_blinken(s,d): #Alle Leds werden auf blinken gestellt (s gibt die geschwindigkeint an, d gibt die wiederholungen an)
    while 0<d:
        d=d-1
        alle_an()
        utime.sleep(1/s)
        alle_aus()
    
#Komplex Befehl difinition

def disco(s,d): #Ein Disco-Modus wird eingeschaltet (s gibt die geschwindigkeint an, d gibt die wiederholungen an)
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

#----Code ab Hier------------------------------------------------------------------------------


disco(15,500)
