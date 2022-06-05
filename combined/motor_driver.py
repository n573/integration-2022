from bluedot import BlueDot
import motor as mot
from time import sleep
from signal import pause
#import grab
bd = BlueDot()

def dpad(pos):
    if pos.top:
        mot.forward()
        mot.speed_up(int(pos.y*100))
    elif pos.right:
        #print(pos.x)
        mot.right(int(pos.x*100))
    elif pos.left:
        #print(pos.x)
        mot.left(int(-pos.x*100))
    elif pos.bottom:
        mot.backward()
        mot.speed_up(int(-pos.y*100))
    #elif pos.middle:
    #    mot.pin.coast()
    else:
        mot.pin.coast()
        #sleep(1)
bd.when_moved = dpad
#bd.when_pressed = grab
pause()
