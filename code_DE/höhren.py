#Mit diesem Code wird die vom Ultraschallsensor erkannte Distanz in cm angegeben
from ultrasonic import Ultra #Importiere die Funktion Ultra
ultra = Ultra(16)



def dis(d):
 while ultra.getDist() > d:
   pass
 stop()
 
dis(1)#passe diesen Wert an um die mindest Distanz festzulegen