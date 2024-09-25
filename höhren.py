from ultrasonic import Ultra
ultra = Ultra(16)
# Drive 


def dis(d):
 while ultra.getDist() > d:
   pass
 stop()
 
dis(1)