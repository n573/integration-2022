from bluedot import BlueDot
import motor as mot
from time import sleep
from signal import pause
bd = BlueDot()

def dpad(pos):
    if (pos.y > 0): #top
        mot.forward()
        mot.speed_up(int(pos.y*100))
    elif (pos.y < 0):
        mot.backward()
        mot.speed_up(int(-pos.y*100))
    #elif pos.middle:
    #    mot.pin.coast()
    else:
        mot.pin.coast()
        #sleep(1)
bd.when_moved = dpad
#bd.when_pressed = mot.pin.coast()
pause()
