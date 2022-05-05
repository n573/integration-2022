from bluedot import BlueDot
import motor as mot
from time import sleep
from signal import pause
bd = BlueDot()

mot.pin.p1.start(0)
mot.pin.p2.start(0)
def dpad(pos):
    if pos.top:
        mot.forward(int(pos.y*100))
    elif pos.right:
        mot.right(int(pos.x*100))
    elif pos.left:
        mot.left(int(-pos.x*100))
    elif pos.bottom:
        mot.backward(int(-pos.y*100))
    else:
        mot.pin.coast()
        #sleep(1)
bd.when_moved = dpad


pause()